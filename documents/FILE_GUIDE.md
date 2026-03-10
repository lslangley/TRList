# 📚 File Guide - Complete Reference

## Project Overview

The Transit App Royale Scraper consists of multiple files organized by purpose.
Use this guide to understand what each file does and how to use it.

---

## 🔧 Core Scripts (Python)

### `scraper.py` - Web Scraper
**Purpose:** Fetches and parses Transit App Royale agencies from the website

**When to use:**
- First-time data collection
- Manual data updates
- Testing the scraper

**How to use:**
```bash
python scraper.py
```

**Output:**
- `transit_agencies.csv`
- `transit_agencies.json`
- `scrape_log.txt` (updated)

**What it does:**
1. Fetches HTML from website
2. Parses with BeautifulSoup
3. Extracts agency information
4. Organizes by country/state
5. Saves to CSV and JSON
6. Logs results

---

### `scheduler.py` - Task Scheduler
**Purpose:** Schedules scraper to run automatically every Monday at 10:00 AM

**When to use:**
- Want automatic updates without Task Scheduler
- Cross-platform scheduling
- Easy monitoring

**How to use:**
```bash
python scheduler.py
```
*Keep this window open while scheduler runs*

**Output:**
- Runs `scraper.py` automatically
- Runs `dashboard.py` automatically
- `scheduler_log.txt` (updated)

**What it does:**
1. Waits for Monday at 10:00 AM
2. Calls scraper.py
3. Calls dashboard.py
4. Logs activity
5. Waits for next Monday

---

### `dashboard.py` - Dashboard Generator
**Purpose:** Creates interactive HTML dashboard from CSV/JSON data

**When to use:**
- After running scraper
- To refresh dashboard display
- To update HTML after data changes

**How to use:**
```bash
python dashboard.py
```

**Output:**
- `index.html` (regenerated)

**What it does:**
1. Reads transit_agencies.json
2. Reads transit_agencies.csv
3. Generates HTML structure
4. Adds CSS styling
5. Includes JavaScript for interactivity
6. Writes index.html

---

### `run.py` - Command Utility
**Purpose:** Simplified interface for running common commands

**When to use:**
- Quick access to common operations
- Batch operations (scraper + dashboard)

**How to use:**
```bash
python run.py scrape        # Run scraper
python run.py dashboard     # Generate dashboard
python run.py both          # Run scraper and dashboard
python run.py schedule      # Start scheduler
python run.py help          # Show options
```

**Available commands:**
- `scrape` - Run scraper only
- `dashboard` - Generate dashboard only
- `both` - Run scraper and generate dashboard
- `schedule` - Start scheduler
- `help` - Show help message

---

## 🛠️ Setup & Configuration

### `requirements.txt` - Dependencies
**Purpose:** Lists all Python packages needed

**Content:**
- `requests` - HTTP library for web scraping
- `beautifulsoup4` - HTML parsing
- `schedule` - Task scheduling
- `pytz` - Timezone support

**How to use:**
```bash
python -m pip install -r requirements.txt
```

---

### `config.ini` - Configuration File
**Purpose:** Centralized settings for all components

**Sections:**
- `[SCRAPER]` - Scraper settings
- `[SCHEDULER]` - Scheduler settings  
- `[OUTPUT]` - File locations
- `[DASHBOARD]` - Dashboard settings
- `[NOTIFICATIONS]` - Email alerts (optional)

**How to use:**
- Edit settings as needed
- Scripts read from this file
- Change URLs, paths, schedules here

**Example edits:**
```ini
# Change schedule to Tuesday:
day = 1

# Change schedule to 2:00 PM:
hour = 14

# Enable dashboard auto-generation:
auto_regenerate = True
```

---

### `quickstart.bat` - One-Click Setup
**Purpose:** Automatically sets up everything for first-time use

**How to use:**
- Double-click `quickstart.bat`
- Or run in Command Prompt:
  ```batch
  quickstart.bat
  ```

**What it does:**
1. Installs dependencies
2. Runs scraper
3. Generates dashboard
4. Creates all necessary files

**Best for:**
- First-time setup
- Quick automated installation

---

### `setup_scheduled_task.bat` - Windows Task Scheduler Setup
**Purpose:** Creates Windows Task Scheduler job for automation

**How to use:**
- **Must run as Administrator**
- Right-click Command Prompt → Run as Administrator
- Navigate to project folder
- Run: `setup_scheduled_task.bat`

**What it does:**
1. Finds Python installation
2. Creates Task Scheduler job
3. Schedules for Monday 10:00 AM
4. Sets retry logic

**Output:**
- Scheduled task in Windows Task Scheduler
- View: Task Scheduler > Task Scheduler Library > Microsoft > Windows
- Or search "task scheduler" and look for "Transit Royale Scraper"

---

### `setup_scheduled_task.ps1` - PowerShell Setup
**Purpose:** PowerShell version of Task Scheduler setup

**How to use:**
- **Must run as Administrator**
- Right-click PowerShell → Run as Administrator
- Navigate to project folder
- Run: `.\setup_scheduled_task.ps1`

**What it does:**
- Same as batch file, with more output
- Better for troubleshooting
- Verifies Python installation

**Advantages:**
- More detailed confirmation
- Better error reporting
- Modern PowerShell approach

---

### `setup_environment.ps1` - Environment Verification
**Purpose:** Checks and verifies system setup

**How to use:**
```powershell
.\setup_environment.ps1
```

**What it checks:**
1. Python installation
2. Python version
3. pip availability
4. Required packages

**Options:**
```powershell
.\setup_environment.ps1 -Install
# Attempts to install Python if not found
```

---

### `.gitignore` - Git Ignore File
**Purpose:** Specifies which files to exclude from version control

**Excludes:**
- Generated data files
- Log files
- Python cache files
- IDE settings
- OS files
- Virtual environments

**When it matters:**
- If using Git version control
- Prevents committing large/sensitive files

---

## 📖 Documentation

### `README.md` - Main Documentation
**Content:**
- Project overview
- Installation instructions
- Usage guide
- Data format documentation
- Troubleshooting
- Development info

**Best for:**
- Comprehensive reference
- Understanding all features
- Detailed troubleshooting

**Size:** ~400 lines

---

### `SETUP_INSTRUCTIONS.md` - Setup Guide
**Content:**
- Step-by-step installation
- Python installation guide
- Package installation
- First-time scrape
- Automatic scheduling setup
- Troubleshooting

**Best for:**
- First-time setup
- Windows-specific instructions
- Detailed step-by-step guidance

**Size:** ~300 lines

---

### `GETTING_STARTED.md` - Quick Start
**Content:**
- Quick 5-minute start
- File overview
- Common commands
- Dashboard features
- Data flow diagram
- Next steps

**Best for:**
- Quick reference
- Command overview
- Getting up to speed fast

**Size:** ~200 lines

---

### `PROJECT_CHECKLIST.md` - Project Summary
**Content:**
- Complete checklist
- Features implemented
- Project structure
- Setup options
- Testing guide
- Troubleshooting

**Best for:**
- Project overview
- Verifying completion
- Testing guide
- Checklists

**Size:** ~250 lines

---

### `FILE_GUIDE.md` - This File
**Content:**
- Complete file reference
- Purpose of each file
- How to use each file
- File interactions

**Best for:**
- Understanding project structure
- Quick file lookup
- Understanding dependencies

---

## 🧪 Testing & Utilities

### `test_system.py` - System Test
**Purpose:** Verifies all components are working

**When to use:**
- After installation
- Before setting up scheduler
- After making changes
- Troubleshooting issues

**How to use:**
```bash
python test_system.py
```

**Tests:**
1. Python module imports
2. Scraper functionality
3. Dashboard generation
4. Log file creation

**Output:**
- Detailed test results
- Pass/Fail summary
- Recommendations

---

### `create_sample_data.py` - Sample Data Generator
**Purpose:** Creates demo data for testing without internet

**When to use:**
- Testing dashboard offline
- Troubleshooting without website access
- Development/testing

**How to use:**
```bash
python create_sample_data.py
```

**Output:**
- `transit_agencies_sample.csv`
- `transit_agencies_sample.json`

**To use the sample:**
```bash
# Rename files for production
ren transit_agencies_sample.csv transit_agencies.csv
ren transit_agencies_sample.json transit_agencies.json

# Then generate dashboard
python dashboard.py
```

---

## 📊 Generated Output Files

### `transit_agencies.csv` - Spreadsheet Data
**Format:** Comma-separated values

**Columns:**
- `Country` - Country/region name
- `State_Province` - State/province
- `Location` - City or area
- `Agency_Name` - Transit agency name
- `Last_Updated` - Timestamp

**Uses:**
- Import to Excel
- Import to Google Sheets
- Database import
- Analytics tools

**Size:** ~50-100 KB

---

### `transit_agencies.json` - JSON Data
**Format:** JavaScript Object Notation

**Structure:**
```json
{
  "Country": {
    "State": ["Agency 1", "Agency 2", ...]
  }
}
```

**Uses:**
- Web applications
- APIs
- Programmatic access
- JavaScript/Python scripts

**Size:** ~30-50 KB

---

### `index.html` - Interactive Dashboard
**Type:** HTML + CSS + JavaScript

**Features:**
- Interactive search
- Country filtering
- Collapsible sections
- Statistics display
- Responsive design
- Mobile-friendly

**How to use:**
- Open in any web browser
- No server needed
- No internet needed (once generated)

**Size:** ~200-300 KB

---

### `scrape_log.txt` - Scraper Log
**Content:** Timestamped scraper activity

**Example entries:**
```
[2024-03-06 10:05:20] ============================================================
[2024-03-06 10:05:20] Transit App Royale Scraper Started
[2024-03-06 10:05:21] Starting scrape...
[2024-03-06 10:05:23] Successfully scraped data for 5 regions
[2024-03-06 10:05:23] Saved 456 agencies to transit_agencies.csv
```

**Uses:**
- Monitor scraper activity
- Troubleshoot issues
- Verify successful runs
- Performance tracking

---

### `scheduler_log.txt` - Scheduler Log
**Content:** Timestamped scheduler activity

**Example entries:**
```
[2024-03-06 08:00:00] ============================================================
[2024-03-06 08:00:00] Scheduler started
[2024-03-06 08:00:00] Scheduled: Every Monday at 10:00 AM PST
[2024-03-06 08:00:00] Next scheduled run: 2024-03-11 10:00:00 PST
```

**Uses:**
- Monitor scheduler activity
- Verify scheduled runs
- Troubleshoot automation
- Confirm next run time

---

## 🔄 File Relationships

```
requirements.txt ──┐
                   ├──> Installation
quickstart.bat ────┘
                   
scraper.py ────> transit_agencies.csv ──┐
               terminal_agencies.json ──┤
               ├> scrape_log.txt        ├──> dashboard.py ──> index.html
               └──────────────────────┘

scheduler.py ──> (runs scraper.py) ──> scheduler_log.txt

run.py ──> (runs scraper.py and/or dashboard.py)

config.ini ──> (settings used by all scripts)

Documentation:        Testing:          Setup:
- README.md          - test_system.py  - setup_scheduled_task.bat
- GETTING_STARTED.md - create_sample   - setup_scheduled_task.ps1
- SETUP_INSTRUCTIONS - create_sample   - setup_environment.ps1
- PROJECT_CHECKLIST  - data.py
- FILE_GUIDE.md
```

---

## 📋 File Checklist

After installation, you should have:

**Python Scripts:**
- [ ] scraper.py
- [ ] scheduler.py
- [ ] dashboard.py
- [ ] run.py
- [ ] test_system.py
- [ ] create_sample_data.py

**Setup Files:**
- [ ] requirements.txt
- [ ] config.ini
- [ ] quickstart.bat
- [ ] setup_scheduled_task.bat
- [ ] setup_scheduled_task.ps1
- [ ] setup_environment.ps1
- [ ] .gitignore

**Documentation:**
- [ ] README.md
- [ ] SETUP_INSTRUCTIONS.md
- [ ] GETTING_STARTED.md
- [ ] PROJECT_CHECKLIST.md
- [ ] FILE_GUIDE.md

**Generated Files (after first run):**
- [ ] transit_agencies.csv
- [ ] transit_agencies.json
- [ ] index.html
- [ ] scrape_log.txt
- [ ] scheduler_log.txt

---

## ✨ Quick Reference

### To set up:
```bash
quickstart.bat
```

### To scrape:
```bash
python scraper.py
```

### To view dashboard:
1. Generate: `python dashboard.py`
2. Open: `index.html` in browser

### To automate:
```bash
# As Administrator:
setup_scheduled_task.bat
```

### To test:
```bash
python test_system.py
```

### To monitor:
```bash
type scrape_log.txt
type scheduler_log.txt
```

---

**For more information, see the individual documentation files.**
