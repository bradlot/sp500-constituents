import sys
import urllib.request
import pandas as pd

try:
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req) as response:
        df = pd.read_html(response)[0]
        
    df['Symbol'].to_csv('sp500.csv', index=False, header=False)
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    sys.exit(1)
