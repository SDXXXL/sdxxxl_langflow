# Auto Load Nodes Script
# Automatically load all custom components for Langflow

$ErrorActionPreference = "Stop"

$customComponentsPath = "c:\Codes\LANG\sdxxxl_langflow\custom_components"
$envVarName = "LANGFLOW_COMPONENTS_PATH"

function Write-Status {
    param([string]$Message)
    Write-Host "[LOAD] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Write-Warn {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

function Copy-CustomComponents {
    param(
        [string]$SourceBasePath,
        [string]$TargetBasePath
    )

    $categories = Get-ChildItem -Path $SourceBasePath -Directory -ErrorAction SilentlyContinue

    if ($categories.Count -eq 0) {
        Write-Warn "No category directories found in: $SourceBasePath"
        return
    }

    Write-Status "Found $($categories.Count) category(ies) to process"

    foreach ($category in $categories) {
        $sourcePath = $category.FullName
        $targetPath = Join-Path $TargetBasePath $category.Name

        if ($sourcePath -eq $targetPath) {
            Write-Host "    -> $($category.Name): Skipped (same location)" -ForegroundColor Gray
            continue
        }

        try {
            Write-Host -NoNewline "    -> $($category.Name): " -ForegroundColor Gray

            $parentPath = Split-Path -Path $targetPath -Parent
            if (-not (Test-Path $parentPath)) {
                New-Item -Path $parentPath -ItemType Directory -Force | Out-Null
            }

            if (Test-Path $targetPath) {
                robocopy "$sourcePath" "$targetPath" /MIR /R:3 /W:5 /MT:8 /NFL /NDL /NJH /NJS | Out-Null
            } else {
                robocopy "$sourcePath" "$targetPath" /E /R:3 /W:5 /MT:8 /NFL /NDL /NJH /NJS | Out-Null
            }

            Write-Host "OK" -ForegroundColor Green
        } catch {
            Write-Host "FAILED" -ForegroundColor Red
            Write-ErrorMsg "  $($_.Exception.Message)"
        }
    }
}

Write-Status "Starting auto load nodes for custom components..."

if (-not (Test-Path $customComponentsPath)) {
    Write-ErrorMsg "Source path does not exist: $customComponentsPath"
    Write-Host "Please ensure custom_components directory is present." -ForegroundColor Yellow
    exit 1
}

$existingPath = [System.Environment]::GetEnvironmentVariable($envVarName, "User")

if ($existingPath) {
    Write-Status "Environment variable $envVarName is already set: $existingPath"
    Copy-CustomComponents -SourceBasePath $customComponentsPath -TargetBasePath $existingPath
    Write-Success "All components have been synced!"
} else {
    Write-Status "Environment variable $envVarName is not set"

    try {
        Write-Status "Setting $envVarName to: $customComponentsPath"
        [System.Environment]::SetEnvironmentVariable($envVarName, $customComponentsPath, "User")
        Write-Success "Environment variable $envVarName has been set"
        Write-Host ""
        Write-Host "IMPORTANT: Please restart your terminal or log out/in for changes to take effect." -ForegroundColor Yellow
        Write-Host ""
    } catch {
        Write-ErrorMsg "Failed to set environment variable: $($_.Exception.Message)"
        Write-Host "Please try running this script as administrator" -ForegroundColor Yellow
        exit 1
    }
}

Write-Success "Node auto load completed!"
Write-Host ""
Write-Host "You can now start Langflow." -ForegroundColor Yellow
Write-Host "Command: langflow run" -ForegroundColor Yellow
Write-Host ""
