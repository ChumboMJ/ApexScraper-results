import requests
from bs4 import BeautifulSoup

url = 'https://www.wmclub.org/wp-content/uploads/2024/12/2024standings.htm'

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Use a GET request to retrieve the site page
response = requests.get(url, headers=headers)

# Check if the request was a success
if response.status_code == 200:
    print("Request was a success!")

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the standings
    table = soup.find_all('table')

    if len(table) < 3:
        raise ValueError(f"Error: {table.count} tables found. There should be at least 3. Verify URL and page to be scraped")

    if table[2]:
        raceResultTable = table[2]

        #Extract the table headers
        headers = [header.text for header in raceResultTable.find_all('th')]
        
        print(headers)
else:
    print("Request was unsuccessful")

print(url)