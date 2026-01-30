#!/usr/bin/env pwsh
# ============================================================================
# Langflow Proxy Launcher (PowerShell)
# Usage: .\start_langflow_proxy.ps1
# ============================================================================

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$configFile = Join-Path $scriptDir "config.ini"

# Load configuration from config.ini

$config = @{
    CONDA_ENV = "lang-env"
    CONDA_PATH = "$env:USERPROFILE\anaconda3"
    PROXY_HTTP = "http://127.0.0.1:7890"
    PROXY_HTTPS = "http://127.0.0.1:7890"
    PROXY_SOCKS = "socks5://127.0.0.1:7890"
    LANGFLOW_HOST = "127.0.0.1"
    LANGFLOW_PORT = "7860"
}

if (Test-Path $configFile) {
    Write-Host "[*] Loading configuration from config.ini..." -ForegroundColor Yellow
    Get-Content $configFile | Where-Object { $_ -match '^\w+=' } | ForEach-Object {
        $parts = $_ -split '=', 2
        if ($parts.Count -eq 2) {
            $config[$parts[0].Trim()] = $parts[1].Trim()
        }
    }
    Write-Host "[*] Configuration loaded successfully" -ForegroundColor Yellow
} else {
    Write-Host "[*] config.ini not found, using default settings" -ForegroundColor Yellow
}

Write-Host "`n[*] Current Configuration:" -ForegroundColor Cyan
Write-Host "   Conda Environment: $($config.CONDA_ENV)" -ForegroundColor Gray
Write-Host "   Conda Path:        $($config.CONDA_PATH)" -ForegroundColor Gray
Write-Host "   HTTP Proxy:        $($config.PROXY_HTTP)" -ForegroundColor Gray
Write-Host "   HTTPS Proxy:       $($config.PROXY_HTTPS)" -ForegroundColor Gray
Write-Host "   Langflow Host:     $($config.LANGFLOW_HOST)" -ForegroundColor Gray
Write-Host "   Langflow Port:     $($config.LANGFLOW_PORT)" -ForegroundColor Gray

# Apply proxy settings
Write-Host "`n[*] Setting proxy environment variables..." -ForegroundColor Yellow
$env:HTTP_PROXY = $config.PROXY_HTTP
$env:HTTPS_PROXY = $config.PROXY_HTTPS
$env:ALL_PROXY = $config.PROXY_SOCKS
$env:http_proxy = $config.PROXY_HTTP
$env:https_proxy = $config.PROXY_HTTPS
$env:all_proxy = $config.PROXY_SOCKS

# Initialize conda environment
Write-Host "`n[*] Initializing conda environment..." -ForegroundColor Yellow
$condaScript = Join-Path $scriptDir "init_conda.ps1"
if (Test-Path $condaScript) {
    . $condaScript -EnvName $config.CONDA_ENV
    if (-not $script:condaInitialized) {
        Write-Host "[!] Warning: Failed to initialize conda environment" -ForegroundColor Yellow
    }
} else {
    Write-Host "[!] Warning: init_conda.ps1 not found, skipping conda initialization" -ForegroundColor Yellow
}

# Verify activation
Write-Host "[*] Verifying Python environment..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "   Python: $pythonVersion" -ForegroundColor Gray
} catch {
    Write-Host "   [!] Warning: Could not verify Python environment" -ForegroundColor Yellow
}

# Run Langflow
Write-Host "`n[*] Starting Langflow..." -ForegroundColor Yellow
Write-Host "   Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host "" -ForegroundColor Gray

# Change to script directory and run langflow
Set-Location $scriptDir
langflow run --host $config.LANGFLOW_HOST --port $config.LANGFLOW_PORT
