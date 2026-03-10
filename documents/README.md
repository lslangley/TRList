# Transit App Royale Clients Scraper

An automated Python system that scrapes the Transit App Royale transit agencies list and displays it on an interactive HTML dashboard. Runs every Monday at 10:00 AM Pacific Standard Time.

## Features

- **Automated Scraping**: Extracts transit agencies from the Transit App help page
- **Scheduled Execution**: Runs automatically every Monday at 10:00 AM PST
- **CSV Export**: Saves data to a searchable CSV file
- **Interactive Dashboard**: Beautiful HTML dashboard with search and filtering
- **Logging**: Comprehensive logging for monitoring and debugging

## Project Structure

```
TRList/                         # repository root
├── scripts/                   # all executable scripts
│   ├── scraper.py             # Main web scraper
│   ├── scheduler.py           # Scheduler for automatic runs
│   ├── dashboard.py           # Dashboard generator
│   ├── run.py                 # Utility wrapper (scrape, dashboard, schedule)
│   ├── create_sample_data.py  # helper for generating fake data
│   ├── test_system.py         # simple sanity‑check tests
│   ├── *.ps1, *.bat           # setup helpers for Windows
│   └── …                      # other scripts
├── documents/                # markdown documentation, guides, notes
├── data/                     # generated outputs (CSV, JSON, HTML, etc.)
├── logs/                     # runtime log files
├── config.ini                # configuration settings
├── requirements.txt          # Python dependencies
└── .gitignore                # version control ignore rules
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Windows (for Task Scheduler integration)

### Step 1: Install Dependencies

```bash
# Navigate to the project directory
cd "c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\TRList"

# Install required packages
pip install -r requirements.txt
```

### Step 2: Run the Scraper Manually (First Time)

```bash
cd scripts
python scraper.py
```

This will:
1. Scrape the Transit App Royale agencies list
2. Save data to `transit_agencies.csv`
3. Save raw data to `transit_agencies.json`
4. Create a log entry in `scrape_log.txt`

### Step 3: Generate the Dashboard

```bash
cd scripts
python dashboard.py
```

This will create `index.html` at the repository root - open it in a web browser to view the interactive dashboard.

## Setting Up Automatic Scheduling

### Option A: Windows Task Scheduler (Recommended)

#### Using the Setup Script:

1. Run the setup script (admin required):
   ```bash
   setup_scheduled_task.bat
   ```
   
   This creates a Windows Task Scheduler job that runs `scheduler.py` at startup.

#### Manual Setup:

1. **Open Task Scheduler** (search "Task Scheduler" in Windows)

2. **Create a new Basic Task:**
   - Name: "Transit Royale Scraper"
   - Description: "Scrape Transit App Royale agencies every Monday at 10 AM PST"

3. **Trigger - New:**
   - Weekly
   - Recur every: 1 week
   - Select: Monday
   - Set time: 10:00:00 AM

4. **Action - New:**
   - Action: Start a program
   - Program/script: `python.exe` (full path, e.g., `C:\Python311\python.exe`)
   - Add arguments: `"scheduler.py"` (or full path to scheduler.py)
   - Start in: `C:\Users\leslie.langley\OneDrive - Transpo Group\Repos\Transit_Royal`

5. **Conditions:**
   - Uncheck "Start the task only if the computer is on AC power" (optional)
   - Uncheck "Stop if the computer switches to battery power" (optional)

6. **Settings:**
   - Check "Run the task as soon as scheduled after a scheduled start is missed"
   - Check "If the task fails, restart every: 10 minutes"

### Option B: Python APScheduler (Cross-Platform)

Run the scheduler manually in the background:

```bash
python scheduler.py
```

If you want this to run on startup, create a batch file `run_scheduler.bat`:

```batch
@echo off
cd "c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\Transit_Royal"
python scheduler.py
pause
```

Then create a shortcut to this batch file in:
`C:\Users\[YourUsername]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## Usage

### 1. Run Scraper Immediately
```bash
python scraper.py
```

### 2. Generate Dashboard
```bash
python dashboard.py
```

### 3. View the Dashboard
Open `index.html` (at the project root) in your web browser. The dashboard features:
- Search bar for filtering agencies
- Country/Region dropdown filter
- Statistics panel showing total agencies and regions
- Collapsible country sections
- Organized by State/Province
- Responsive design for mobile and desktop

## Data Files

### CSV Format (transit_agencies.csv)
```
Country,State_Province,Location,Agency_Name,Last_Updated
United States,California,Bakersfield CA,Golden Empire Transit District / GET Bus,2024-03-06 10:05:23
United States,California,Bakersfield CA,Kern Transit,2024-03-06 10:05:23
...
```

### JSON Format (transit_agencies.json)
```json
{
  "United States": {
    "California": [
      "Bakersfield, CA – Golden Empire Transit District / GET Bus",
      "Bakersfield, CA – Kern Transit",
      ...
    ]
  },
  "Canada": {...},
  ...
}
```

## Logs

### Scraper Log (scrape_log.txt)
Contains detailed information about each scrape:
```
[2024-03-06 10:05:20] ============================================================
[2024-03-06 10:05:20] Transit App Royale Scraper Started
[2024-03-06 10:05:21] Starting scrape...
[2024-03-06 10:05:23] Successfully scraped data for 5 regions
[2024-03-06 10:05:23] Saved 456 agencies to transit_agencies.csv
[2024-03-06 10:05:23] Saved data to transit_agencies.json
```

### Scheduler Log (scheduler_log.txt)
Contains scheduler events:
```
[2024-03-06 08:00:00] ============================================================
[2024-03-06 08:00:00] Scheduler started - Transit App Royale Scraper
[2024-03-06 08:00:00] Scheduled: Every Monday at 10:00 AM PST
[2024-03-06 08:00:00] Next scheduled run: 2024-03-11 10:00:00 PST
```

## Troubleshooting

### Issue: "Module not found" error
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Scheduler not running
**Solution:** 
1. Check that the Task Scheduler task is enabled
2. Verify the path to python.exe is correct
3. Check scheduler_log.txt for errors

### Issue: No data being scraped
**Solution:**
1. Check if the website structure has changed
2. View the website: https://help.transitapp.com/article/436-transit-agencies-gifting-royale-to-their-riders
3. Update the scraper parsing logic if needed
4. Check scrape_log.txt for error messages

### Issue: Permission denied when creating Task Scheduler task
**Solution:** Run Command Prompt or PowerShell as Administrator

## Updating to Match Website Changes

If the website structure changes and the scraper stops working:

1. Visit the source URL in a browser
2. Inspect the HTML structure (F12 key)
3. Update the parsing logic in `scraper.py`
4. Test with `python scraper.py`
5. Regenerate dashboard with `python dashboard.py`

## Deployment

### Deploy to Cloud (Optional)

For continuous monitoring without depending on your computer:

- **Azure Functions**: Deploy scraper as serverless function with Time trigger
- **AWS Lambda**: Similar to Azure, triggered by CloudWatch Events
- **Heroku**: Deploy scheduler with Heroku Scheduler add-on
- **Render**: Free-tier deployment with background workers

Both `scraper.py` and `dashboard.py` can be deployed independently.

## Development

### Running All Steps
```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
python scraper.py

# Generate dashboard
python dashboard.py

# Optional: Start scheduler for live updates
python scheduler.py
```

### Testing the Scraper
```bash
# Test scraper manually
python scraper.py

# Check the generated files
# - Opens transit_agencies.csv in Excel/text editor
# - Opens index.html in browser
```

## Source Data

**Website**: https://help.transitapp.com/article/436-transit-agencies-gifting-royale-to-their-riders

**Data Updated**: Weekly (This script scrapes every Monday at 10:00 AM PST)

## License

This project scrapes publicly available data from Transit App's help center for informational purposes.

## Support

For issues or improvements:
1. Check the log files (`scrape_log.txt`, `scheduler_log.txt`)
2. Review the website to see if it has changed
3. Verify all dependencies are installed
4. Test the scraper manually: `python scraper.py`

## Future Enhancements

- [ ] Email notifications on successful scrape
- [ ] Slack integration for updates
- [ ] Database storage (SQLite, PostgreSQL)
- [ ] API endpoint for accessing data
- [ ] Email alerts on data changes
- [ ] Historical data tracking
- [ ] Duplicate detection across agencies
- [ ] Export to Excel format
