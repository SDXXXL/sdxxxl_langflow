$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$configFile = Join-Path $scriptDir "config.ini"

$config = @{
    LANGFLOW_CACHE_PATH = "C:/Users/$env:USERNAME/AppData/Local/langflow/langflow/Cache"
}

if (Test-Path $configFile) {
    Write-Host "[FIX] Loading configuration from config.ini..." -ForegroundColor Yellow
    Get-Content $configFile | Where-Object { $_ -match '^\w+=' } | ForEach-Object {
        $parts = $_ -split '=', 2
        if ($parts.Count -eq 2) {
            $config[$parts[0].Trim()] = $parts[1].Trim()
        }
    }
    Write-Host "[FIX] Configuration loaded successfully" -ForegroundColor Yellow
} else {
    Write-Host "[FIX] config.ini not found, using default settings" -ForegroundColor Yellow
}

$langflowCachePath = [System.Environment]::ExpandEnvironmentVariables($config.LANGFLOW_CACHE_PATH)
$langflowCachePath = $langflowCachePath.Replace('/', '\')
$secretKeyPath = Join-Path $langflowCachePath "secret_key"

function Write-Status {
    param([string]$Message)
    Write-Host "[FIX] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

function Reset-FilePermissions {
    param(
        [string]$Path,
        [string]$Username
    )

    $permissions = @(
        "${Username}:(OI)(CI)F",
        "Everyone:(OI)(CI)F",
        "BUILTIN\Administrators:(OI)(CI)F",
        "SYSTEM:(OI)(CI)F"
    )

    foreach ($perm in $permissions) {
        cmd /c "icacls `"$Path`" /grant:r `"$perm`"" 2>&1 | Out-Null
    }
}

function Test-FileAccess {
    param([string]$Path)

    try {
        $testStream = [System.IO.File]::Open(
            $Path,
            [System.IO.FileMode]::Open,
            [System.IO.FileAccess]::ReadWrite,
            [System.IO.FileShare]::None
        )
        $testStream.Close()
        $testStream.Dispose()
        return $true
    }
    catch {
        return $false
    }
}

function Ask-YesNo {
    param([string]$Message)

    do {
        $answer = Read-Host "$Message (yes/no)"
        if ($answer -eq "yes") {
            return $true
        }
        elseif ($answer -eq "no") {
            return $false
        }
        else {
            Write-Host "Please enter 'yes' or 'no'" -ForegroundColor Yellow
        }
    } while ($true)
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Magenta
Write-Host "  Langflow Permission Fix Script" -ForegroundColor Magenta
Write-Host "============================================" -ForegroundColor Magenta
Write-Host ""

if (-not (Test-Path $langflowCachePath)) {
    Write-Status "Cache directory does not exist, creating..."
    New-Item -Path $langflowCachePath -ItemType Directory -Force | Out-Null
}

if (Test-Path $secretKeyPath) {
    Write-Warning "The secret_key file exists and will be modified."
    Write-Host ""
    Write-Host "After unlocking, the secret_key file will be accessible without" -ForegroundColor Yellow
    Write-Host "requiring special permissions. This means any user on this computer" -ForegroundColor Yellow
    Write-Host "can read this file, which contains sensitive key data." -ForegroundColor Yellow
    Write-Host ""
    Write-Warning "Please ensure this computer is secure and only trusted users have"
    Write-Warning "access to your account."
    Write-Host ""

    if (-not (Ask-YesNo "Do you want to continue unlocking?")) {
        Write-Host "Operation cancelled by user." -ForegroundColor Yellow
        exit 0
    }
}
else {
    Write-Status "secret_key file does not exist, no unlock needed."
}

Write-Host ""
Write-Status "Starting permission fix process..."
Write-Host ""

try {
    $username = [System.Environment]::GetEnvironmentVariable("USERNAME")

    Write-Status "Taking ownership of directory..."
    takeown /f $langflowCachePath /r /d y 2>&1 | Out-Null

    if (Test-Path $secretKeyPath) {
        Write-Status "Attempting non-destructive fix (preserving secret_key)..."
        Write-Host ""

        Write-Status "Taking ownership of secret_key file..."
        takeown /f $secretKeyPath 2>&1 | Out-Null

        Write-Status "Resetting file permissions..."
        Reset-FilePermissions -Path $secretKeyPath -Username $username

        $permissionFixSuccess = $false

        if (Test-FileAccess -Path $secretKeyPath) {
            Write-Success "File access restored! secret_key preserved."
            $permissionFixSuccess = $true
        }
        else {
            Write-Status "File still inaccessible, resetting ACL..."
            cmd /c "icacls `"$secretKeyPath`" /reset" 2>&1 | Out-Null
            cmd /c "icacls `"$secretKeyPath`" /grant:r `"${username}:(F)`"" 2>&1 | Out-Null

            if (Test-FileAccess -Path $secretKeyPath) {
                Write-Success "File access restored after resetting ACL! secret_key preserved."
                $permissionFixSuccess = $true
            }
            else {
                Write-Status "Trying force method..."
                cmd /c "icacls `"$secretKeyPath`" /setowner `"${username}`"" 2>&1 | Out-Null
                cmd /c "icacls `"$secretKeyPath`" /grant:r `"${username}:F`" /T" 2>&1 | Out-Null

                if (Test-FileAccess -Path $secretKeyPath) {
                    Write-Success "File access restored! secret_key preserved."
                    $permissionFixSuccess = $true
                }
            }
        }

        if (-not $permissionFixSuccess) {
            Write-Host ""
            Write-ErrorMsg "Could not restore file access."
            Write-Host ""
            Write-Host "The secret_key file may be corrupted or locked by another process." -ForegroundColor Yellow
            Write-Host ""
            Write-Warning "DESTRUCTIVE METHOD: Delete secret_key file"
            Write-Host ""
            Write-Host "This will delete the secret_key file. All stored global variable" -ForegroundColor Red
            Write-Host "keys and credentials will be LOST and cannot be recovered!" -ForegroundColor Red
            Write-Host ""
            Write-Host "You will need to reconfigure any external API keys and credentials" -ForegroundColor Yellow
            Write-Host "that were stored in Langflow's global variables." -ForegroundColor Yellow
            Write-Host ""

            if (Ask-YesNo "Do you want to delete secret_key and lose all stored keys?") {
                Write-Host ""
                Write-Status "Deleting secret_key file..."
                $acl = Get-Acl $secretKeyPath
                $acl.SetAccessRuleProtection($false, $false)
                Set-Acl -Path $secretKeyPath -AclObject $acl 2>&1 | Out-Null
                Remove-Item $secretKeyPath -Force -ErrorAction Stop
                Write-Success "secret_key file deleted. All stored keys have been lost."
            }
            else {
                Write-Host ""
                Write-Status "Skipped destructive method. The permission issue remains unresolved."
                Write-Host "Try closing Langflow and run this script again as administrator." -ForegroundColor Yellow
            }
        }
    }

    Write-Host ""
    Write-Status "Resetting directory permissions..."
    Reset-FilePermissions -Path $langflowCachePath -Username $username

    Write-Host ""
    Write-Success "Permission fix completed!"
    Write-Host ""
    Write-Host "You can now start Langflow." -ForegroundColor Yellow
    Write-Host "Command: langflow run" -ForegroundColor Yellow
    Write-Host ""

} catch {
    Write-ErrorMsg "Error during fix: $($_.Exception.Message)"
    Write-Host ""
    Write-Host "Please try running this script as administrator" -ForegroundColor Yellow
    exit 1
}
