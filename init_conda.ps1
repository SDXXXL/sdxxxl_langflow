#!/usr/bin/env pwsh
# ============================================================================
# Conda Environment Initialization Script
# Usage: . .\init_conda.ps1 [-EnvName <name>]
# ============================================================================

param(
    [string]$EnvName
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$configFile = Join-Path $scriptDir "config.ini"

$config = @{
    CONDA_ENV = "lang-env"
    CONDA_PATH = "$env:USERPROFILE\anaconda3"
}

function Write-Status {
    param([string]$Message)
    Write-Host "[CONDA] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Load-Config {
    if (Test-Path $configFile) {
        Get-Content $configFile | Where-Object { $_ -match '^\w+=' } | ForEach-Object {
            $parts = $_ -split '=', 2
            if ($parts.Count -eq 2) {
                $key = $parts[0].Trim()
                $value = $parts[1].Trim()
                if ($config.ContainsKey($key)) {
                    $config[$key] = $value
                }
            }
        }
    }
}

function Get-CondaExePath {
    $condaPath = $config.CONDA_PATH.Replace('\', '/').Replace('C:/', 'C:\')

    $possiblePaths = @(
        (Join-Path $condaPath "condabin\conda.exe"),
        (Join-Path $condaPath "Scripts\conda.exe"),
        (Join-Path $condaPath "conda.exe")
    )

    foreach ($path in $possiblePaths) {
        if (Test-Path $path) {
            return $path
        }
    }

    $cmdPath = Get-Command "conda" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($cmdPath) {
        return $cmdPath.Source
    }

    return $null
}

function Import-CondaModule {
    param([string]$CondaExePath)

    $condaRoot = Split-Path -Parent $CondaExePath

    $modulePaths = @(
        (Join-Path $condaRoot "shell\condabin\Conda.psm1"),
        (Join-Path $condaRoot "..\shell\condabin\conda-hook.ps1")
    )

    foreach ($modulePath in $modulePaths) {
        $resolvedPath = (Get-Item $modulePath -ErrorAction SilentlyContinue).FullName
        if ($resolvedPath -and (Test-Path $resolvedPath)) {
            try {
                if ($resolvedPath -like "*Conda.psm1") {
                    $CondaModuleArgs = @{ChangePs1 = $True}
                    Import-Module $resolvedPath -ArgumentList $CondaModuleArgs -ErrorAction Stop
                    Remove-Variable CondaModuleArgs
                    return $true
                }
                else {
                    & "$resolvedPath" | Out-Null
                    return $true
                }
            }
            catch {
                Write-ErrorMsg "Failed to import conda module: $($_.Exception.Message)"
            }
        }
    }

    return $false
}

function Initialize-CondaEnvironment {
    param([string]$TargetEnv)

    Load-Config

    if ($TargetEnv) {
        $config.CONDA_ENV = $TargetEnv
    }

    $condaExe = Get-CondaExePath
    if (-not $condaExe) {
        Write-ErrorMsg "Conda executable not found. Please check CONDA_PATH in config.ini"
        return $false
    }

    Write-Status "Found conda at: $condaExe"

    $env:CONDA_EXE = $condaExe
    $env:_CONDA_EXE = $condaExe
    $env:CONDA_PYTHON_EXE = Join-Path (Split-Path -Parent $condaExe) "python.exe"
    $env:_CONDA_ROOT = Split-Path -Parent $condaExe

    $imported = Import-CondaModule -CondaExePath $condaExe
    if (-not $imported) {
        Write-Status "Using command-line activation"
    }

    try {
        conda activate $config.CONDA_ENV
        return $true
    }
    catch {
        Write-ErrorMsg "Failed to activate environment: $($_.Exception.Message)"
        return $false
    }
}

$script:condaInitialized = Initialize-CondaEnvironment -EnvName $EnvName

if ($script:condaInitialized) {
    Write-Success "Conda environment '$($config.CONDA_ENV)' activated"
}
else {
    Write-ErrorMsg "Failed to initialize conda environment"
}

return $script:condaInitialized
