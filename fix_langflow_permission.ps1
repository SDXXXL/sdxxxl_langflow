# Langflow Permission Fix Script
# 解决 Windows 上 Langflow 权限拒绝问题

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

Write-Status "开始修复 Langflow 权限问题..."

# 检查路径是否存在
if (-not (Test-Path $langflowCachePath)) {
    Write-Status "缓存目录不存在，正在创建..."
    New-Item -Path $langflowCachePath -ItemType Directory -Force | Out-Null
}

try {
    # 步骤1: 获取目录所有权（递归）
    Write-Status "获取目录所有权..."
    takeown /f $langflowCachePath /r /d y 2>&1 | Out-Null

    # 步骤2: 强制删除旧的 secret_key 文件
    if (Test-Path $secretKeyPath) {
        Write-Status "删除旧的 secret_key 文件..."
        $acl = Get-Acl $secretKeyPath
        $acl.SetAccessRuleProtection($false, $false)
        Set-Acl -Path $secretKeyPath -AclObject $acl 2>&1 | Out-Null
        Remove-Item $secretKeyPath -Force -ErrorAction Stop
    }

    # 步骤3: 重置目录权限
    Write-Status "重置目录权限..."
    $username = [System.Environment]::GetEnvironmentVariable("USERNAME")

    # 使用 icacls 重置并添加权限
    $commands = @(
        "/remove:d $username",
        "/grant:r $username:(OI)(CI)F",
        "/grant:r Everyone:(OI)(CI)F",
        "/grant:r BUILTIN\Administrators:(OI)(CI)F",
        "/grant:r SYSTEM:(OI)(CI)F"
    )

    foreach ($cmd in $commands) {
        icacls "$langflowCachePath $cmd" 2>&1 | Out-Null
    }

    Write-Success "权限修复完成！"
    Write-Host ""
    Write-Host "现在可以启动 Langflow 了。" -ForegroundColor Yellow
    Write-Host "命令: langflow run" -ForegroundColor Yellow
    Write-Host ""

} catch {
    Write-ErrorMsg "修复过程中出现错误: $($_.Exception.Message)"
    Write-Host ""
    Write-Host "请尝试以管理员身份运行此脚本" -ForegroundColor Yellow
    exit 1
}
