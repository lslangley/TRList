# PowerShell script to verify and set up the Transit Royale Scraper environment

param([switch]$Install = $false)

function Write-Header {
    param([string]$Text)
    Write-Host "`n" + ("=" * 60) -ForegroundColor Cyan
    Write-Host "  $Text" -ForegroundColor Cyan
    Write-Host ("=" * 60) -ForegroundColor Cyan
}

function Test-Python {
    $python = Get-Command python.exe -ErrorAction SilentlyContinue
    if ($python) {
        try {
            $version = & python.exe --version 2>&1
            return $version
        } catch {
            return $null
        }
    }
    return $null
}

function Install-Python {
    Write-Host "`nInstalling Python from Microsoft Store..." -ForegroundColor Yellow
    try {
        # This requires Windows 10/11 and winget
        winget install Python.Python.3.11 -e --accept-source-agreements --accept-package-agreements
        Write-Host "Python installation initiated. Please complete the installation." -ForegroundColor Green
        Write-Host "After installation, close and reopen PowerShell, then run this script again." -ForegroundColor Green
    } catch {
        Write-Host "Error: Could not install Python automatically." -ForegroundColor Red
        Write-Host "Please download and install Python manually from:" -ForegroundColor Yellow
        Write-Host "  https://www.python.org/downloads/" -ForegroundColor Yellow
        Write-Host "`nMake sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    }
}

Write-Header "Transit Royale Scraper - Environment Setup"

Write-Host "`nChecking environment requirements..." -ForegroundColor Yellow

# Check Python
$pythonVersion = Test-Python
if ($pythonVersion) {
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python not found" -ForegroundColor Red
    
    if ($Install) {
        Install-Python
        exit
    } else {
        Write-Host "`nTo install Python, run: .\setup_environment.ps1 -Install" -ForegroundColor Yellow
        Write-Host "`nOr download and install manually from: https://www.python.org/downloads/" -ForegroundColor Yellow
        exit 1
    }
}

# Get Python path
$pythonPath = (Get-Command python.exe).Source
Write-Host "  Location: $pythonPath" -ForegroundColor Gray

# Check pip
Write-Host "`nChecking pip..." -ForegroundColor Yellow
try {
    $pipVersion = & python.exe -m pip --version
    Write-Host "✓ pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ pip not found" -ForegroundColor Red
    Write-Host "  Attempting to install pip..." -ForegroundColor Yellow
    & python.exe -m ensurepip --upgrade
}

# Check required packages
Write-Host "`nChecking required packages..." -ForegroundColor Yellow

$packages = @("requests", "beautifulsoup4", "schedule", "pytz")
$missing = @()

foreach ($package in $packages) {
    try {
        & python.exe -c "import $($package.Replace('-', '_'))" 2>$null
        Write-Host "✓ $package" -ForegroundColor Green
    } catch {
        Write-Host "✗ $package - Missing" -ForegroundColor Yellow
        $missing += $package
    }
}

if ($missing.Count -gt 0) {
    Write-Host "`nInstalling missing packages..." -ForegroundColor Yellow
    & python.exe -m pip install @missing
    Write-Host "✓ Packages installed" -ForegroundColor Green
} else {
    Write-Host "`n✓ All packages installed" -ForegroundColor Green
}

# Final status
Write-Header "Setup Complete"

Write-Host "`nYour Transit Royale Scraper is ready!" -ForegroundColor Green

Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "  1. Run the scraper: python scraper.py" -ForegroundColor Gray
Write-Host "  2. Generate dashboard: python dashboard.py" -ForegroundColor Gray
Write-Host "  3. Or run both: python run.py both" -ForegroundColor Gray
Write-Host "`nOptional:" -ForegroundColor Cyan
Write-Host "  Set up automatic scheduling: .\setup_scheduled_task.ps1" -ForegroundColor Gray

Write-Host "`nFor more information, see: README.md`n" -ForegroundColor Gray
