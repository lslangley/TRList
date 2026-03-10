# Setup Instructions - Transit App Royale Scraper

## System Requirements

- **Operating System**: Windows 10/11
- **Python**: 3.7 or higher
- **RAM**: 256 MB minimum
- **Disk Space**: 10 MB

## Installation Steps

### Step 1: Download and Install Python

1. **Check if Python is already installed:**
   - Open Command Prompt or PowerShell
   - Type: `python --version`
   - If you see a version number like "Python 3.11.x", skip to Step 2

2. **If Python is not installed:**
   - Go to https://www.python.org/downloads/
   - Download the latest Python 3.11+ installer
   - **IMPORTANT**: During installation, check ✓ "Add Python to PATH"
   - Click "Install Now" and wait for completion
   - Restart your computer

3. **Verify Installation:**
   - Open Command Prompt
   - Type: `python --version`
   - You should see: `Python 3.11.x` (or similar)

### Step 2: Clone/Download the Project

The project is located at:
```
c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\TRList
```

### Step 3: Install Python Packages

1. **Open Command Prompt or PowerShell**
   - Navigate to project directory:
     ```
     cd "c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\TRList"
     ```

2. **Run the setup:**
   - **Option A - Automatic (Recommended):**
     - Double-click `quickstart.bat`
     - This will install packages and run your first scrape automatically

   - **Option B - Manual:**
     ```
     python -m pip install -r requirements.txt
     ```

### Step 4: Run Your First Scrape

#### Automatic Way (Recommended):
- Double-click `quickstart.bat`
- This will install dependencies and generate your dashboard

#### Manual Way:

1. **Open Command Prompt in the project directory**

2. **Change into the scripts folder:**
   ```
   cd scripts
   ```

3. **Run the scraper:**
   ```
   python scraper.py
   ```
   - Output files will be saved under `../data/` (CSV/JSON)
   - Check `../logs/scrape_log.txt` for detailed logs

4. **Generate the dashboard:**
   ```
   python dashboard.py
   ```
   - This writes `index.html` to the repository root

5. **View the dashboard:**
   - Open `index.html` in your web browser
   - Use the search and filter features to explore agencies

### Step 5: Set Up Automatic Scheduling (Optional)

Choose one method:

#### Method A: Windows Task Scheduler (Recommended) - Using Batch File

1. **Open Command Prompt as Administrator:**
   - Right-click Command Prompt
   - Select "Run as Administrator"

2. **Navigate to the project:**
   ```
   cd "c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\Transit_Royal"
   ```

3. **Run the setup script:**
   ```
   setup_scheduled_task.bat
   ```
   - This creates a Windows Task that runs every Monday at 10:00 AM

4. **Verify the task was created:**
   - Open Task Scheduler (search "Task Scheduler" in Windows)
   - Look for "Transit Royale Scraper" in the list
   - It should show next run time as next Monday at 10:00 AM

#### Method B: Windows Task Scheduler - Using PowerShell

1. **Open PowerShell as Administrator:**
   - Right-click PowerShell
   - Select "Run as Administrator"

2. **Navigate to the project:**
   ```
   cd "c:\Users\leslie.langley\OneDrive - Transpo Group\Repos\Transit_Royal"
   ```

3. **Run the setup script:**
   ```
   .\setup_scheduled_task.ps1
   ```

4. **If you get an execution policy error:**
   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   - Then run the setup script again

#### Method C: Manual Scheduling Using Python Scheduler

1. **Open Command Prompt**

2. **Run the scheduler:**
   ```
   python scheduler.py
   ```
   - Keep this window open
   - The scheduler will run scrape tasks automatically
   - You can minimize but not close the window

## Usage

### Run Scraper Immediately
```
python scraper.py
```

### Run Dashboard Generator
```
python dashboard.py
```

### Run Both Scraper and Dashboard
```
python run.py both
```

### Start the Scheduler
```
python scheduler.py
```

### View Dashboard
1. Open `index.html` in a web browser (located at repo root)
2. Use the search box to find agencies
3. Click on country headers to expand/collapse sections
4. Use the country dropdown to filter

## Outputs

After running the scraper, you'll have:

| File | Description |
|------|-------------|
| `transit_agencies.csv` | Comma-separated values with agency data |
| `transit_agencies.json` | JSON format for programmatic access |
| `index.html` | Interactive web dashboard (located at project root) |
| `scrape_log.txt` | Scraper execution logs |
| `scheduler_log.txt` | Scheduler execution logs |

## Troubleshooting

### Issue: "Python command not found"
**Solution:**
1. Check if Python is installed: `python --version`
2. If not found, reinstall Python ensuring "Add to PATH" is checked
3. Restart Command Prompt or your computer

### Issue: "ModuleNotFoundError" when running scraper
**Solution:**
```
python -m pip install -r requirements.txt
```

### Issue: Certificate error when scraping
**Solution:**
- This is a common macOS issue, less common on Windows
- If it occurs, try:
  ```
  pip install --upgrade certifi
  /Applications/Python\ 3.11/Install\ Certificates.command
  ```

### Issue: Task Scheduler task won't run
**Solution:**
1. Open Task Scheduler
2. Right-click "Transit Royale Scraper"
3. Select "Run"
4. Check the result in "Last Run Result"
5. Review logs in `scheduler_log.txt` and `scrape_log.txt`

### Issue: Website data format changed
**Solution:**
1. Visit the source website in browser
2. The website structure may have changed
3. Update the parsing logic in `scraper.py`
4. Contact support or file an issue

## Maintenance

### Manual Updates
To update data manually at any time:
```
python scraper.py
python dashboard.py
```

### Viewing Logs
Check log files to diagnose issues:
- `scrape_log.txt` - Scraper activity
- `scheduler_log.txt` - Scheduler activity

### CSV Data
The `transit_agencies.csv` file can be imported into:
- Excel
- Google Sheets
- Microsoft Access
- Any database system

## Support

### Check Logs First
Most issues are logged in:
- `scrape_log.txt`
- `scheduler_log.txt`

### Common Fixes
1. Verify Python is installed: `python --version`
2. Reinstall packages: `python -m pip install -r requirements.txt`
3. Check internet connection
4. Verify the source website is accessible
5. Check Windows Task Scheduler (if using automatic scheduling)

## Next Steps

1. ✓ Python installed
2. ✓ Packages installed
3. ✓ First scrape completed
4. ✓ Dashboard generated
5. ✓ Automatic scheduling configured (optional)
6. → You're all set! 

The system will now run automatically every Monday at 10:00 AM PST and update the CSV and dashboard.

---

**Questions?** Check the [README.md](README.md) for more detailed documentation.
