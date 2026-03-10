"""
Sample data generator - Creates sample data for testing the dashboard
Useful if you want to test the dashboard without internet access
"""

import json
import csv
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
JSON_FILE = SCRIPT_DIR / "transit_agencies_sample.json"
CSV_FILE = SCRIPT_DIR / "transit_agencies_sample.csv"

def create_sample_data():
    """Create sample transit agencies data"""
    
    sample_data = {
        "United States": {
            "California": [
                "Bakersfield, CA – Golden Empire Transit District / GET Bus",
                "Bakersfield, CA – Kern Transit",
                "Berkeley, CA – Bear Transit (University of California, Berkeley)",
                "Fairfield, CA – FAST Fairfield and Suisun Transit",
                "Monterey, CA – Monterey-Salinas Transit",
                "Orange County, CA – OC Bus (Orange County Transportation Authority)",
                "Pasadena, CA – Pasadena Transit",
                "Petaluma, CA – Petaluma Transit",
                "Santa Clara, CA – VTA (Santa Clara Valley Transportation Authority)",
                "Santa Cruz, CA – Santa Cruz METRO",
                "Santa Rosa, CA – Santa Rosa CityBus",
            ],
            "Colorado": [
                "Aspen, CO – Snowmass Village Shuttle",
                "Breckenridge, CO – Breck Free Ride",
                "Summit County, CO – Summit Stage",
                "Telluride, CO – SMART",
            ],
            "Florida": [
                "Miami, FL – Miami Beach Trolleys",
                "Naples, FL – Collier Area Transit",
                "Orlando, FL - LYNX",
                "Pinellas County, FL – PSTA (Pinellas Suncoast Transit Authority)",
                "Tampa, FL – Hillsborough Transit Authority",
                "West Palm Beach, FL – Palm Tran (sponsored by WBPgo)",
            ],
            "New York": [
                "Lewis County, NY – Lewis County Transit",
                "Suffolk County, NY – Suffolk County Transit",
            ],
            "Texas": [
                "Austin, TX – CapMetro",
                "Austin, TX – CARTS",
                "Denton County, TX – DCTA",
                "Laredo, TX – El Metro",
                "San Antonio, TX – VIA Metropolitan Transit",
            ],
        },
        "Canada": {
            "Alberta": [
                "Airdrie, AB - Airdrie Transit",
                "Banff, AB – Roam Transit",
                "Calgary, AB – Calgary Transit",
            ],
            "Ontario": [
                "Belleville, ON – Belleville Transit",
                "Brantford, ON – Brantford Transit",
                "Kingston, ON – Kingston Transit",
                "Ottawa, ON – OC Transpo",
                "Thunder Bay, ON – Thunder Bay Transit",
            ],
        },
        "International": {
            "France": [
                "Châlons-en-Champagne, FR – SITAC",
                "Dreux, FR – Linéad",
            ],
            "Ireland": [
                "Dublin, IE – Dublin Commuter Coalition",
            ],
        }
    }
    
    return sample_data

def save_sample_json(data):
    """Save sample data to JSON"""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Sample JSON saved to: {JSON_FILE}")

def save_sample_csv(data):
    """Save sample data to CSV"""
    rows = []
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for country, states in data.items():
        for state, agencies in states.items():
            for agency in agencies:
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
                    'Last_Updated': last_updated
                })
    
    fieldnames = ['Country', 'State_Province', 'Location', 'Agency_Name', 'Last_Updated']
    
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Sample CSV saved to: {CSV_FILE}")
    print(f"Total agencies: {len(rows)}")

if __name__ == "__main__":
    print("Creating sample data...")
    print()
    
    data = create_sample_data()
    save_sample_json(data)
    save_sample_csv(data)
    
    print()
    print("Sample data files created successfully!")
    print()
    print("To use this sample data with the dashboard:")
    print("1. Rename the sample files:")
    print(f"   - Rename '{JSON_FILE}' to 'transit_agencies.json'")
    print(f"   - Rename '{CSV_FILE}' to 'transit_agencies.csv'")
    print("2. Run: python dashboard.py")
    print("3. Open index.html in your browser")
    print()
