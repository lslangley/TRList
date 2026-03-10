# Getting Started - Transit App Royale Scraper

Your scraper is now ready! Here's a quick guide to get you up and running.

## 📋 What You Have

A complete Python system that:
- ✅ Scrapes Transit App Royale agencies from the web
- ✅ Saves data to CSV and JSON formats
- ✅ Creates an interactive HTML dashboard
- ✅ Runs automatically every Monday at 10:00 AM PST
- ✅ Logs all activities for monitoring

## 🚀 Quick Start (5 minutes)

### Step 1: Install Dependencies

**Option A - Automatic (Recommended):**
```
Double-click: quickstart.bat
```

**Option B - Manual:**
Open Command Prompt and run:
```
python -m pip install -r requirements.txt
```

### Step 2: Run Your First Scrape

Open Command Prompt in this directory and run:
```
python scraper.py
```

### Step 3: Generate Dashboard

```
python dashboard.py
```

### Step 4: View Dashboard

Open `index.html` in your web browser.

---

## 📁 Project Files

### Core Scripts
| File | Purpose |
|------|---------|
| `scraper.py` | Fetches data from Transit App website |
| `scheduler.py` | Schedules scraper to run automatically |
| `dashboard.py` | Generates interactive HTML dashboard |
| `run.py` | Utility for running commands |

### Setup & Configuration
| File | Purpose |
|------|---------|
| `requirements.txt` | Python package dependencies |
| `config.ini` | Configuration settings |
| `quickstart.bat` | One-click setup script |
| `setup_scheduled_task.bat` | Create Windows scheduled task |
| `setup_scheduled_task.ps1` | PowerShell version of scheduler setup |
| `setup_environment.ps1` | Verify environment setup |

### Documentation
| File | Purpose |
|------|---------|
| `README.md` | Detailed documentation |
| `SETUP_INSTRUCTIONS.md` | Step-by-step setup guide |
| `GETTING_STARTED.md` | This file |

### Testing & Utilities
| File | Purpose |
|------|---------|
| `test_system.py` | Verify everything is working |
| `create_sample_data.py` | Create demo data |

### Output Files (Generated)
| File | Purpose |
|------|---------|
| `transit_agencies.csv` | Spreadsheet format |
| `transit_agencies.json` | JSON format |
| `index.html` | Interactive dashboard |
| `scrape_log.txt` | Scraper logs |
| `scheduler_log.txt` | Scheduler logs |

---

## 🔧 Common Commands

### Run Scraper
```bash
python scraper.py
```
Fetches fresh data from the website and saves to CSV/JSON.

### Generate Dashboard
```bash
python dashboard.py
```
Creates an interactive HTML file from the CSV/JSON data.

### Run Both
```bash
python run.py both
```
Runs scraper and dashboard in sequence.

### Start Scheduler
```bash
python scheduler.py
```
Starts the Python scheduler (keeps running until stopped).

### Test System
```bash
python test_system.py
```
Verifies all components are working correctly.

### Create Sample Data
```bash
python create_sample_data.py
```
Creates demo data for testing (useful without internet).

---

## ⏰ Automatic Scheduling

Choose one method to have the scraper run automatically every Monday at 10:00 AM PST:

### Method 1: Windows Task Scheduler (Recommended)

**Step 1: Open Command Prompt as Administrator**
- Right-click Command Prompt → "Run as administrator"

**Step 2: Run the setup script**
```batch
setup_scheduled_task.bat
```

**Step 3: Verify**
- Open Task Scheduler
- Search for "Transit Royale Scraper"
- Should show next run as "Next Monday at 10:00 AM"

### Method 2: PowerShell Setup

**Step 1: Open PowerShell as Administrator**
- Right-click PowerShell → "Run as administrator"

**Step 2: Navigate to project**
```powershell
cd "c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\Transit_Royal"
```

**Step 3: Run setup**
```powershell
.\setup_scheduled_task.ps1
```

---

## 📊 Using the Dashboard

The `index.html` dashboard has several features:

### Search
- Type in the search box to filter by agency name, city, or state

### Filter by Country/Region
- Use the dropdown to show only agencies from specific countries

### Expand/Collapse Sections
- Click on country names to expand or collapse agency lists

### Statistics
- View total agency count and regions

### Mobile Friendly
- Works on phones and tablets

---

## 📝 Output Files

### CSV Format (transit_agencies.csv)
```
Country,State_Province,Location,Agency_Name,Last_Updated
United States,California,Bakersfield CA,Golden Empire Transit District / GET Bus,2024-03-06 10:05:23
United States,California,Berkeley CA,Bear Transit (University of California Berkeley),2024-03-06 10:05:23
```

Use this with:
- Excel
- Google Sheets
- Any database
- Any analytics tool

### JSON Format (transit_agencies.json)
```json
{
  "United States": {
    "California": [
      "Bakersfield, CA – Golden Empire Transit District / GET Bus",
      ...
    ]
  }
}
```

Use this for:
- Web applications
- APIs
- Programmatic access

### HTML Dashboard (index.html)
- **Interactive web interface** for exploring agencies
- **Search and filter** capabilities
- **No server required** - pure HTML/JavaScript
- **Responsive** - works on all devices

---

## 🔍 Troubleshooting

### "Python command not found"
```bash
python --version
```
If this fails, reinstall Python from https://www.python.org/

### "Module not found" error
```bash
python -m pip install -r requirements.txt
```

### Scraper not working
1. Check internet connection
2. Visit the website manually: https://help.transitapp.com/article/436-transit-agencies-gifting-royale-to-their-riders
3. Check `scrape_log.txt` for error messages

### Task Scheduler not running
1. Open Task Scheduler
2. Find "Transit Royale Scraper"
3. Right-click → "Run"
4. Check "Last Run Result" for errors

---

## 📊 Scheduling Options

### Option A: Windows Task Scheduler
- ✅ No Python window needed
- ✅ Runs even if user not logged in
- ✅ Works with multiple users
- ❌ Windows only

### Option B: Python Scheduler
- ✅ Works on all operating systems
- ✅ Easy to monitor
- ❌ Requires Python window to stay open
- ❌ Won't run if computer is off

### Option C: Windows Event Scheduler with PowerShell
- ✅ Professional setup
- ✅ Run as System
- ✅ Advanced logging
- ❌ Most complex

---

## 🔄 Data Flow

```
[Website] 
    ↓
[scraper.py] → Fetches & parses HTML
    ↓
[CSV & JSON files] → Raw data storage
    ↓
[dashboard.py] → Generates HTML
    ↓
[index.html] → Interactive dashboard display
```

**Automatically every Monday at 10:00 AM:**
1. Scheduler triggers scraper.py
2. Scraper fetches fresh data
3. Dashboard is auto-regenerated
4. CSV and JSON updated
5. All changes logged

---

## 💾 Data Backup

The CSV file is a good backup format. To backup your data:

```bash
# Create a backup with timestamp
copy transit_agencies.csv "backup_transit_agencies_%date%.csv"
```

Or use cloud storage like OneDrive:
- Files are already in OneDrive sync folder
- Automatic versioning available

---

## ⚙️ Customization

### Change Schedule Time
Edit `scheduler.py`:
```python
schedule.every().monday.at("10:00").do(run_scraper_job)
```

### Change Dashboard Title
Edit `dashboard.py`:
```python
<title>Your Custom Title</title>
```

### Add Custom Styling
Edit the CSS section in `dashboard.py`

---

## 🚀 Next Steps

1. **Test the system:**
   ```
   python test_system.py
   ```

2. **View the dashboard:**
   - Open `index.html` in browser

3. **Set up automatic scheduling:**
   - Run `setup_scheduled_task.bat` (as Administrator)

4. **Optional: Customize configuration:**
   - Edit `config.ini` for your preferences

---

## 📞 Support

### Check Logs
- `scrape_log.txt` - Scraper activity
- `scheduler_log.txt` - Scheduler activity

### Common Issues
See `SETUP_INSTRUCTIONS.md` for troubleshooting

### More Details
See `README.md` for comprehensive documentation

---

## 🎉 You're Ready!

Your Transit App Royale scraper is now set up and ready to use.

**What happens next:**
1. Data will be scraped every Monday at 10:00 AM PST
2. CSV and JSON files automatically updated
3. Dashboard automatically refreshed
4. All activity logged for monitoring

**Questions?** Check the documentation files or examine the code comments for more details.

Happy scraping! 🚌
