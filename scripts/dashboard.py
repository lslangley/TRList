"""
Dashboard generator - Creates an interactive HTML dashboard from scraped data
"""

import json
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# locate base and data folders
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# ensure output directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

JSON_FILE = DATA_DIR / "transit_agencies.json"
CSV_FILE = DATA_DIR / "transit_agencies.csv"
HTML_OUTPUT = BASE_DIR / "index.html"  # dashboard now lives at repo root

def read_json_data():
    """Read the JSON data file"""
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return None

def read_csv_data():
    """Read the CSV data file"""
    try:
        agencies = []
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            agencies = list(reader)
        return agencies
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def generate_statistics(agencies_data):
    """Generate statistics from the data"""
    stats = {
        'total_agencies': 0,
        'total_countries': 0,
        'countries': {},
        'states': {}
    }
    
    for country, states in agencies_data.items():
        if states:  # Skip empty countries
            stats['total_countries'] += 1
            stats['countries'][country] = 0
            
            for state, agencies in states.items():
                if agencies:
                    count = len(agencies)
                    stats['total_agencies'] += count
                    stats['countries'][country] += count
                    
                    if country not in stats['states']:
                        stats['states'][country] = {}
                    stats['states'][country][state] = count
    
    return stats

def generate_html_dashboard(agencies_data, last_updated=None):
    """Generate the interactive HTML dashboard"""
    
    stats = generate_statistics(agencies_data)
    
    # Get last update time
    if not last_updated:
        try:
            with open(CSV_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                if rows:
                    last_updated = rows[0].get('Last_Updated', 'Unknown')
        except:
            last_updated = 'Unknown'
    
    # Build the HTML
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transit App Royale Agencies</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        header {{
            background: white;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }}
        
        header h1 {{
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}
        
        header p {{
            color: #666;
            font-size: 1.1em;
            margin-bottom: 5px;
        }}
        
        .last-updated {{
            color: #999;
            font-size: 0.9em;
            font-style: italic;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        
        .stat-card h3 {{
            color: #999;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
        }}
        
        .stat-card .number {{
            color: #667eea;
            font-size: 2.5em;
            font-weight: bold;
        }}
        
        .controls {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }}
        
        .search-box {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        
        .search-box input,
        .search-box select {{
            padding: 10px 15px;
            border: 2px solid #eee;
            border-radius: 5px;
            font-size: 1em;
            flex: 1;
            min-width: 200px;
        }}
        
        .search-box input:focus,
        .search-box select:focus {{
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.1);
        }}
        
        .search-box button {{
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }}
        
        .search-box button:hover {{
            background: #764ba2;
        }}
        
        .results {{
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }}
        
        .country-section {{
            border-bottom: 1px solid #eee;
        }}
        
        .country-section:last-child {{
            border-bottom: none;
        }}
        
        .country-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: bold;
            font-size: 1.2em;
            user-select: none;
            transition: background 0.3s;
        }}
        
        .country-header:hover {{
            background: linear-gradient(135deg, #5568d3 0%, #653a8a 100%);
        }}
        
        .country-header .toggle {{
            display: inline-block;
            transition: transform 0.3s;
        }}
        
        .country-header.collapsed .toggle {{
            transform: rotate(-90deg);
        }}
        
        .country-content {{
            max-height: 10000px;  /* Large value to allow full expansion */
            overflow: auto;  /* Enable scrolling when content exceeds height */
            transition: max-height 0.3s ease;
        }}
        
        .country-content.collapsed {{
            max-height: 0;
            overflow: hidden;
        }}
        
        .state-group {{
            padding: 20px;
            border-left: 4px solid #667eea;
            margin: 0;
            background: #fafafa;
        }}
        
        .state-group:nth-child(even) {{
            background: white;
        }}
        
        .state-header {{
            color: #667eea;
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 10px;
        }}
        
        .agencies-list {{
            list-style: none;
        }}
        
        .agencies-list li {{
            padding: 8px 0;
            padding-left: 20px;
            color: #333;
            border-left: 2px solid #ddd;
            padding-left: 15px;
        }}
        
        .agencies-list li:hover {{
            background: rgba(102, 126, 234, 0.05);
            border-left-color: #667eea;
        }}
        
        .no-results {{
            padding: 40px 20px;
            text-align: center;
            color: #999;
        }}
        
        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding: 20px;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 1.8em;
            }}
            
            .stats {{
                grid-template-columns: 1fr;
            }}
            
            .search-box {{
                flex-direction: column;
            }}
            
            .search-box input,
            .search-box select {{
                min-width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚌 Transit App Royale Agencies</h1>
            <p>Interactive directory of transit agencies providing free Royale subscriptions</p>
            <p class="last-updated">Last updated: {last_updated}</p>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <h3>Total Agencies</h3>
                <div class="number">{stats['total_agencies']}</div>
            </div>
            <div class="stat-card">
                <h3>Countries/Regions</h3>
                <div class="number">{stats['total_countries']}</div>
            </div>
        </div>
        
        <div class="controls">
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="Search agencies, cities, or states...">
                <select id="countryFilter">
                    <option value="">All Countries/Regions</option>
                    {gen_country_options(agencies_data)}
                </select>
                <button onclick="clearSearch()">Clear</button>
            </div>
        </div>
        
        <div class="results" id="results">
            {gen_results_html(agencies_data)}
        </div>
        
        <div class="footer">
            <p>Data source: <a href="https://help.transitapp.com/article/436-transit-agencies-gifting-royale-to-their-riders" style="color: white; text-decoration: underline;">Transit App Help Center</a></p>
            <p>Last scraped: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>
    </div>
    
    <script>
        const agenciesData = {json.dumps(agencies_data)};
        
        document.getElementById('searchInput').addEventListener('keyup', filterResults);
        document.getElementById('countryFilter').addEventListener('change', filterResults);
        
        function filterResults() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const countryFilter = document.getElementById('countryFilter').value;
            
            const countryElements = document.querySelectorAll('.country-section');
            let anyVisible = false;
            
            countryElements.forEach(section => {{
                const countryName = section.querySelector('.country-header').textContent.trim();
                const states = section.querySelectorAll('.state-group');
                let countryVisible = false;
                
                // Check country filter
                if (countryFilter && !countryName.includes(countryFilter)) {{
                    section.style.display = 'none';
                    return;
                }}
                
                section.style.display = 'block';
                
                states.forEach(state => {{
                    const stateText = state.querySelector('.state-header').textContent.toLowerCase();
                    const agencies = state.querySelectorAll('.agencies-list li');
                    let stateVisible = false;
                    
                    agencies.forEach(agency => {{
                        const text = agency.textContent.toLowerCase();
                        const matches = text.includes(searchTerm) || stateText.includes(searchTerm);
                        agency.style.display = matches || !searchTerm ? 'block' : 'none';
                        if (matches || !searchTerm) {{
                            stateVisible = true;
                        }}
                    }});
                    
                    state.style.display = stateVisible || !searchTerm ? 'block' : 'none';
                    if (stateVisible || !searchTerm) {{
                        countryVisible = true;
                    }}
                }});
                
                if (countryVisible) {{
                    anyVisible = true;
                }}
            }});
            
            const noResults = document.getElementById('noResults');
            if (!anyVisible && searchTerm) {{
                if (!noResults) {{
                    const div = document.createElement('div');
                    div.id = 'noResults';
                    div.className = 'no-results';
                    div.innerHTML = '<p>No agencies found matching your search.</p>';
                    document.getElementById('results').appendChild(div);
                }}
            }} else if (noResults) {{
                noResults.remove();
            }}
        }}
        
        function toggleCountry(header) {{
            header.classList.toggle('collapsed');
            const content = header.nextElementSibling;
            content.classList.toggle('collapsed');
        }}
        
        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('countryFilter').value = '';
            filterResults();
        }}
        
        // Initialize: set up country toggle listeners
        document.querySelectorAll('.country-header').forEach(header => {{
            header.addEventListener('click', function() {{
                toggleCountry(this);
            }});
        }});
    </script>
</body>
</html>
"""
    
    return html_content

def gen_country_options(agencies_data):
    """Generate country filter options"""
    options = ""
    for country in sorted(agencies_data.keys()):
        if agencies_data[country]:  # Only include countries with data
            options += f'<option value="{country}">{country}</option>\n'
    return options

def gen_results_html(agencies_data):
    """Generate the results HTML"""
    html = ""
    
    for country, states in sorted(agencies_data.items()):
        if not states:  # Skip empty countries
            continue
        
        html += f"""
        <div class="country-section">
            <div class="country-header">
                <span>{country}</span>
                <span class="toggle">▼</span>
            </div>
            <div class="country-content">
"""
        
        for state, agencies in sorted(states.items()):
            if agencies:
                html += f"""
                <div class="state-group">
                    <div class="state-header">{state}</div>
                    <ul class="agencies-list">
"""
                for agency in sorted(agencies):
                    html += f"                        <li>{agency}</li>\n"
                
                html += """
                    </ul>
                </div>
"""
        
        html += """
            </div>
        </div>
"""
    
    return html

def generate_dashboard():
    """Main function to generate the dashboard"""
    try:
        print("Generating dashboard...")
        
        # Read the JSON data
        agencies_data = read_json_data()
        if not agencies_data:
            print("No data available. Please run the scraper first.")
            return False
        
        # Generate HTML
        html_content = generate_html_dashboard(agencies_data)
        
        # Write to file
        with open(HTML_OUTPUT, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Dashboard generated successfully: {HTML_OUTPUT}")
        return True
    
    except Exception as e:
        print(f"Error generating dashboard: {e}")
        return False

if __name__ == "__main__":
    generate_dashboard()
