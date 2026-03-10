# PowerShell script to set up Windows Task Scheduler for Transit Royale Scraper
# Run as Administrator: Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

param([switch]$Remove = $false)

$ScriptName = "Transit Royale Scraper"
$TaskName = "Transit Royale Scraper"
$ScriptPath = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
$PythonPath = (Get-Command python.exe).Source
$SchedulerScript = Join-Path $ScriptPath "scheduler.py"

# Check if running as Administrator
$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "Error: This script must be run as Administrator" -ForegroundColor Red
    Write-Host "Please run PowerShell as Administrator and try again" -ForegroundColor Yellow
    exit 1
}

if ($Remove) {
    # Remove the existing task
    Write-Host "Removing existing task..." -ForegroundColor Yellow
    try {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction Stop
        Write-Host "Task removed successfully" -ForegroundColor Green
    } catch {
        Write-Host "Task not found or error removing task: $_" -ForegroundColor Yellow
    }
    exit 0
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Transit Royale Scraper Setup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Verify Python
if (-not $PythonPath) {
    Write-Host "Error: Python not found in PATH" -ForegroundColor Red
    Write-Host "Please install Python and add it to your PATH" -ForegroundColor Yellow
    exit 1
}

Write-Host "Python found: $PythonPath" -ForegroundColor Green
Write-Host "Script location: $SchedulerScript" -ForegroundColor Green
Write-Host "Task name: $TaskName" -ForegroundColor Green

# Remove existing task if it exists
try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
} catch {
    # Task doesn't exist, continue
}

# Create task action
$action = New-ScheduledTaskAction `
    -Execute $PythonPath `
    -Argument "`"$SchedulerScript`""

# Create task trigger for every Monday at 10:00 AM
$trigger = New-ScheduledTaskTrigger `
    -Weekly `
    -DaysOfWeek Monday `
    -At 10:00am

# Create task settings with retry logic
$settings = New-ScheduledTaskSettingsSet `
    -MultipleInstances IgnoreNew `
    -RunOnlyIfNetworkAvailable `
    -StartWhenAvailable `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 10)

# Create the task
try {
    $principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount
    $task = Register-ScheduledTask `
        -TaskName $TaskName `
        -Action $action `
        -Trigger $trigger `
        -Settings $settings `
        -Principal $principal `
        -Force
    
    Write-Host "`n✓ SUCCESS! Scheduled task created" -ForegroundColor Green
    Write-Host "`nTask Configuration:" -ForegroundColor Cyan
    Write-Host "  Name: $TaskName"
    Write-Host "  Schedule: Every Monday at 10:00 AM PST"
    Write-Host "  Script: $SchedulerScript"
    Write-Host "  Python: $PythonPath"
    
    Write-Host "`nNext Run: $(($task.Triggers[0] | Get-Date).ToShortTimeString() + ' on Monday')" -ForegroundColor Cyan
    
    Write-Host "`nTo view task details, run:" -ForegroundColor Yellow
    Write-Host "  Get-ScheduledTask -TaskName `"$TaskName`" | Format-List *" -ForegroundColor Gray
    
    Write-Host "`nTo remove the task later, run:" -ForegroundColor Yellow
    Write-Host "  Unregister-ScheduledTask -TaskName `"$TaskName`"" -ForegroundColor Gray
    
    Write-Host "`nThe scheduler will now run automatically every Monday at 10:00 AM.`n" -ForegroundColor Green
}
catch {
    Write-Host "`n✗ ERROR: Failed to create scheduled task" -ForegroundColor Red
    Write-Host "Error details: $_" -ForegroundColor Red
    Write-Host "`nPlease check:" -ForegroundColor Yellow
    Write-Host "  1. You are running as Administrator"
    Write-Host "  2. Python is properly installed"
    Write-Host "  3. The script path exists: $SchedulerScript"
    exit 1
}
