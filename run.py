"""
Utility script for running various maintenance tasks
Usage: python run.py [command]

Commands:
  scrape         - Run the scraper once
  dashboard      - Generate the HTML dashboard
  both           - Run scraper and generate dashboard
  schedule       - Start the scheduler
  help           - Show this help message
"""

import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SCRAPER_SCRIPT = SCRIPT_DIR / "scraper.py"
DASHBOARD_SCRIPT = SCRIPT_DIR / "dashboard.py"
SCHEDULER_SCRIPT = SCRIPT_DIR / "scheduler.py"

def run_command(script_path):
    """Run a script and return success status"""
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")
        return False
    except FileNotFoundError:
        print(f"Script not found: {script_path}")
        return False

def main():
    if len(sys.argv) < 2:
        command = "help"
    else:
        command = sys.argv[1].lower()

    print("=" * 60)
    print("Transit App Royale Scraper - Utility")
    print("=" * 60)
    print()

    if command == "scrape":
        print("Running scraper...")
        print()
        run_command(SCRAPER_SCRIPT)

    elif command == "dashboard":
        print("Generating dashboard...")
        print()
        run_command(DASHBOARD_SCRIPT)

    elif command == "both":
        print("Running scraper...")
        print()
        scraper_success = run_command(SCRAPER_SCRIPT)

        print()
        print("Generating dashboard...")
        print()
        dashboard_success = run_command(DASHBOARD_SCRIPT)

        print()
        if scraper_success and dashboard_success:
            print("✓ Both operations completed successfully")
        else:
            print("✗ One or more operations failed")

    elif command == "schedule":
        print("Starting scheduler...")
        print("This will run every Monday at 10:00 AM PST")
        print("Press Ctrl+C to stop")
        print()
        run_command(SCHEDULER_SCRIPT)

    elif command == "help" or command == "-h" or command == "--help":
        print(__doc__)

    else:
        print(f"Unknown command: {command}")
        print("\nValid commands:")
        print("  scrape       - Run the scraper once")
        print("  dashboard    - Generate the HTML dashboard")
        print("  both         - Run scraper and generate dashboard")
        print("  schedule     - Start the scheduler")
        print("  help         - Show help")
        print()
        print("Usage: python run.py [command]")

if __name__ == "__main__":
    main()
