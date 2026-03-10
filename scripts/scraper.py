"""
Transit App Royale Clients Scraper
Scrapes the Transit App Royale transit agencies list and saves to CSV
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import json
from pathlib import Path

# Configuration
SCRAPE_URL = "https://help.transitapp.com/article/436-transit-agencies-gifting-royale-to-their-riders"

# Define directories relative to the project root
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

# make sure output folders exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILE = DATA_DIR / "transit_agencies.csv"
JSON_FILE = DATA_DIR / "transit_agencies.json"
LOG_FILE = LOGS_DIR / "scrape_log.txt"

def log_message(message):
    """Log messages to both console and log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

def scrape_transit_agencies():
    """
    Scrape the Transit App Royale agencies list from the website
    Returns a dictionary with country/region keys and state/province keys with agency lists
    """
    try:
        log_message("Starting scrape...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(SCRAPE_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main content area
        content = soup.find('article') or soup.find('div', class_='article-body')
        if not content:
            content = soup.find('div', class_='content')
        
        agencies_data = {
            'United States': {},
            'Canada': {},
            'International': {}
        }
        
        current_country = None
        current_state = None
        agencies_list = []
        
        # Parse the HTML content
        for element in content.find_all(['h3', 'h4', 'p', 'ul', 'li']):
            text = element.get_text(strip=True)
            
            # Detect country headers
            if element.name == 'h3':
                # Check if this is a country header
                if text in ['United States', 'Canada', 'Ireland', 'France', 'New Zealand']:
                    if text in agencies_data:
                        current_country = text
                    else:
                        current_country = 'International'
                    current_state = None
                    agencies_list = []
            
            # Detect state/province headers (could be <h4> or a <p> with bold text)
            elif current_country and (element.name == 'h4' or element.name == 'p'):
                # many pages use <p><strong>StateName</strong></p> instead of h4
                # only treat <p> as header when it contains a strong tag or is short
                state_candidate = text
                is_header = False
                if element.name == 'h4':
                    is_header = True
                elif element.name == 'p':
                    if element.find('strong') is not None:
                        is_header = True
                    else:
                        # avoid random paragraphs that aren't state names
                        # simple heuristic: if it contains no punctuation and is short
                        if len(state_candidate) < 50 and state_candidate.isalpha():
                            is_header = True
                if is_header:
                    current_state = state_candidate
                    if current_country not in agencies_data:
                        agencies_data[current_country] = {}
                    agencies_data[current_country][current_state] = []
                    agencies_list = []
                
            # Parse agency entries (bullet points)
            elif element.name == 'li' and current_country and current_state:
                if ' – ' in text or ' - ' in text:
                    # Split city/region and agency name
                    agency_entry = text.strip()
                    if agency_entry and agency_entry not in agencies_data[current_country][current_state]:
                        agencies_data[current_country][current_state].append(agency_entry)
        
        log_message(f"Successfully scraped data for {len(agencies_data)} regions")
        return agencies_data
    
    except requests.RequestException as e:
        log_message(f"Error fetching website: {e}")
        return None
    except Exception as e:
        log_message(f"Error parsing data: {e}")
        return None

def flatten_agencies_data(agencies_data):
    """
    Flatten the nested structure into a list of rows for CSV
    """
    rows = []
    
    for country, states in agencies_data.items():
        for state, agencies in states.items():
            for agency in agencies:
                # Parse agency entry to extract city and agency name
                if ' – ' in agency:
                    location, name = agency.split(' – ', 1)
                elif ' - ' in agency:
                    location, name = agency.split(' - ', 1)
                else:
                    location = agency
                    name = agency
                
                rows.append({
                    'Country': country,
                    'State_Province': state,
                    'Location': location.strip(),
                    'Agency_Name': name.strip(),
                    'Last_Updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
    
    return rows

def save_to_csv(rows):
    """Save the scraped data to CSV file"""
    try:
        if not rows:
            log_message("No data to save")
            return False
        
        fieldnames = ['Country', 'State_Province', 'Location', 'Agency_Name', 'Last_Updated']
        
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        log_message(f"Saved {len(rows)} agencies to {CSV_FILE}")
        return True
    except Exception as e:
        log_message(f"Error saving to CSV: {e}")
        return False

def save_to_json(agencies_data):
    """Save the scraped data to JSON file"""
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(agencies_data, f, indent=2, ensure_ascii=False)
        log_message(f"Saved data to {JSON_FILE}")
        return True
    except Exception as e:
        log_message(f"Error saving to JSON: {e}")
        return False

def run_scraper():
    """Main scraper function"""
    try:
        # Create log file if it doesn't exist
        if not LOG_FILE.exists():
            LOG_FILE.touch()
        
        log_message("=" * 60)
        log_message("Transit App Royale Scraper Started")
        
        # Scrape the data
        agencies_data = scrape_transit_agencies()
        
        if not agencies_data:
            log_message("Scraping failed, exiting")
            return False
        
        # Flatten and save to CSV
        rows = flatten_agencies_data(agencies_data)
        csv_success = save_to_csv(rows)
        
        # Save to JSON as well (for the dashboard)
        json_success = save_to_json(agencies_data)
        
        log_message("Scraper completed successfully")
        log_message("=" * 60)
        
        return csv_success and json_success
    
    except Exception as e:
        log_message(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    run_scraper()
