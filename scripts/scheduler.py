"""
Scheduler for scraping Transit App Royale agencies
Runs the scraper every Monday at 10:00 AM Pacific Standard Time
"""

import schedule
import time
from datetime import datetime
import subprocess
import sys
from pathlib import Path
import pytz

# directories
SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent
LOGS_DIR = BASE_DIR / "logs"
SCRAPER_SCRIPT = SCRIPT_DIR / "scraper.py"
LOG_FILE = LOGS_DIR / "scheduler_log.txt"

# ensure logs folder exists
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Pacific Time Zone
PACIFIC_TZ = pytz.timezone('US/Pacific')

def log_message(message):
    """Log messages to both console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

def run_scraper_job():
    """Execute the scraper script"""
    try:
        log_message("Running scheduled scraper job...")
        result = subprocess.run(
            [sys.executable, str(SCRAPER_SCRIPT)],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            log_message("Scraper job completed successfully")
        else:
            log_message(f"Scraper job failed with return code {result.returncode}")
            if result.stderr:
                log_message(f"Error output: {result.stderr}")
    except subprocess.TimeoutExpired:
        log_message("Scraper job timed out after 300 seconds")
    except Exception as e:
        log_message(f"Error running scraper job: {e}")

def schedule_scraper():
    """Schedule the scraper to run every Monday at 10:00 AM PST"""
    # Schedule every Monday at 10:00 AM
    schedule.every().monday.at("10:00").do(run_scraper_job)
    
    log_message("=" * 60)
    log_message("Scheduler started - Transit App Royale Scraper")
    log_message("Scheduled: Every Monday at 10:00 AM PST")
    log_message("=" * 60)

def get_next_run_time():
    """Calculate the next scheduled run time"""
    import schedule as sched
    # This is a simplified check - in production you might want more sophisticated logic
    now = datetime.now(PACIFIC_TZ)
    days_until_monday = (7 - now.weekday()) % 7  # 0 = Monday
    if days_until_monday == 0 and now.hour >= 10:
        days_until_monday = 7
    
    next_run = now.replace(hour=10, minute=0, second=0, microsecond=0)
    if days_until_monday == 0:
        next_run = now.replace(hour=10, minute=0, second=0, microsecond=0)
    else:
        from datetime import timedelta
        next_run = now + timedelta(days=days_until_monday)
        next_run = next_run.replace(hour=10, minute=0, second=0, microsecond=0)
    
    return next_run

def main():
    """Main scheduler loop"""
    try:
        # Create log file if it doesn't exist
        if not LOG_FILE.exists():
            LOG_FILE.touch()
        
        schedule_scraper()
        next_run = get_next_run_time()
        log_message(f"Next scheduled run: {next_run.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        
        # Keep scheduler running
        log_message("Scheduler is now running. Press Ctrl+C to stop.")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    except KeyboardInterrupt:
        log_message("Scheduler stopped by user")
    except Exception as e:
        log_message(f"Unexpected error in scheduler: {e}")

if __name__ == "__main__":
    main()
