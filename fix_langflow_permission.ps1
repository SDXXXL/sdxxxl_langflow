# Langflow Permission Fix Script
# Fix Langflow permission denied issues on Windows

$ErrorActionPreference = "Stop"

$langflowCachePath = "C:\Users\$env:USERNAME\AppData\Local\langflow\langflow\Cache"
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

Write-Status "Starting Langflow permission fix..."

# Check if path exists
if (-not (Test-Path $langflowCachePath)) {
    Write-Status "Cache directory does not exist, creating..."
    New-Item -Path $langflowCachePath -ItemType Directory -Force | Out-Null
}

try {
    # Step 1: Take ownership of directory (recursive)
    Write-Status "Taking ownership of directory..."
    takeown /f $langflowCachePath /r /d y 2>&1 | Out-Null

    # Step 2: Force delete old secret_key file
    if (Test-Path $secretKeyPath) {
        Write-Status "Deleting old secret_key file..."
        $acl = Get-Acl $secretKeyPath
        $acl.SetAccessRuleProtection($false, $false)
        Set-Acl -Path $secretKeyPath -AclObject $acl 2>&1 | Out-Null
        Remove-Item $secretKeyPath -Force -ErrorAction Stop
    } else {
        Write-Status "secret_key file already deleted (may have been removed in previous run)"
    }

    # Step 3: Reset directory permissions
    Write-Status "Resetting directory permissions..."
    $username = [System.Environment]::GetEnvironmentVariable("USERNAME")

    # Use icacls to grant full control permissions
    $permissions = @(
        "${username}:(OI)(CI)F",
        "Everyone:(OI)(CI)F",
        "BUILTIN\Administrators:(OI)(CI)F",
        "SYSTEM:(OI)(CI)F"
    )

    foreach ($perm in $permissions) {
        cmd /c "icacls `"$langflowCachePath`" /grant:r `"$perm`"" 2>&1 | Out-Null
    }

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
