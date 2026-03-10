"""
Test script to verify the Transit Royale Scraper is working correctly
Run this before setting up automatic scheduling
"""

import sys
import subprocess
from pathlib import Path
import time

SCRIPTS_DIR = Path(__file__).parent
BASE_DIR = SCRIPTS_DIR.parent

SCRAPER_SCRIPT = SCRIPTS_DIR / "scraper.py"
DASHBOARD_SCRIPT = SCRIPTS_DIR / "dashboard.py"

def test_imports():
    """Test that all required modules can be imported"""
    print("=" * 60)
    print("Testing Python module imports...")
    print("=" * 60)
    
    required_modules = {
        'requests': 'requests',
        'beautifulsoup4': 'bs4',
        'schedule': 'schedule',
        'pytz': 'pytz',
    }
    
    all_ok = True
    
    for package, module in required_modules.items():
        try:
            __import__(module.split('.')[0])
            print(f"✓ {package:20} OK")
        except ImportError as e:
            print(f"✗ {package:20} FAILED - {e}")
            all_ok = False
    
    if not all_ok:
        print("\nError: Some modules are missing.")
        print("Run: python -m pip install -r requirements.txt")
        return False
    
    print("\n✓ All modules imported successfully\n")
    return True

def test_scraper():
    """Test the scraper"""
    print("=" * 60)
    print("Testing scraper...")
    print("=" * 60)
    print()
    
    try:
        result = subprocess.run(
            [sys.executable, str(SCRAPER_SCRIPT)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✓ Scraper executed successfully")
            
            # Check if output files were created
            csv_file = BASE_DIR / "data" / "transit_agencies.csv"
            json_file = BASE_DIR / "data" / "transit_agencies.json"
            
            if csv_file.exists():
                size = csv_file.stat().st_size
                print(f"✓ CSV file created: {size:,} bytes")
            else:
                print("✗ CSV file not created")
                return False
            
            if json_file.exists():
                size = json_file.stat().st_size
                print(f"✓ JSON file created: {size:,} bytes")
            else:
                print("✗ JSON file not created")
                return False
            
            print()
            return True
        else:
            print(f"✗ Scraper failed with exit code {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            print()
            return False
    
    except subprocess.TimeoutExpired:
        print("✗ Scraper timed out (took longer than 30 seconds)")
        print()
        return False
    except Exception as e:
        print(f"✗ Error running scraper: {e}")
        print()
        return False

def test_dashboard():
    """Test the dashboard generator"""
    print("=" * 60)
    print("Testing dashboard generation...")
    print("=" * 60)
    print()
    
    try:
        result = subprocess.run(
            [sys.executable, str(DASHBOARD_SCRIPT)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print("✓ Dashboard generator executed successfully")
            
            # Check if HTML file was created
            html_file = BASE_DIR / "index.html"
            
            if html_file.exists():
                size = html_file.stat().st_size
                print(f"✓ HTML file created: {size:,} bytes")
                print(f"  Location: {html_file}")
                print()
                return True
            else:
                print("✗ HTML file not created")
                print()
                return False
        else:
            print(f"✗ Dashboard generator failed with exit code {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            print()
            return False
    
    except subprocess.TimeoutExpired:
        print("✗ Dashboard generator timed out")
        print()
        return False
    except Exception as e:
        print(f"✗ Error running dashboard generator: {e}")
        print()
        return False

def test_logs():
    """Check log files"""
    print("=" * 60)
    print("Testing logs...")
    print("=" * 60)
    print()
    
    log_file = BASE_DIR / "logs" / "scrape_log.txt"
    
    if log_file.exists():
        print(f"✓ Log file exists: {log_file}")
        
        # Read last few lines
        with open(log_file, 'r') as f:
            lines = f.readlines()
            if lines:
                print(f"  Recent entries:")
                for line in lines[-5:]:
                    print(f"    {line.rstrip()}")
        print()
        return True
    else:
        print("✗ Log file not found")
        print()
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  Transit Royale Scraper - System Test".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    results = {
        'Imports': test_imports(),
        'Scraper': test_scraper(),
        'Dashboard': test_dashboard(),
        'Logs': test_logs(),
    }
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print()
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status:10} {test_name}")
        if not passed:
            all_passed = False
    
    print()
    print("=" * 60)
    
    if all_passed:
        print("✓ All tests passed! System is ready for automatic scheduling.")
        print()
        print("Next steps:")
        print("  1. View the dashboard: Open index.html in a browser")
        print("  2. Set up automatic scheduling:")
        print("     - On Windows: Run setup_scheduled_task.bat (as Administrator)")
        print("     - Or: Run scheduler.py to start manual scheduler")
        print()
        return 0
    else:
        print("✗ Some tests failed. Please check the output above.")
        print()
        print("Troubleshooting:")
        print("  1. Ensure Python is installed: python --version")
        print("  2. Install dependencies: python -m pip install -r requirements.txt")
        print("  3. Check internet connection for web scraping")
        print("  4. Review log files for detailed error information")
        print()
        return 1

if __name__ == "__main__":
    exit_code = main()
    
    print("Press Enter to exit...")
    input()
    
    sys.exit(exit_code)
