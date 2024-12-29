import requests
from bs4 import BeautifulSoup
import json

# Script used for scraping event data, including individual run information

url = 'https://www.wmclub.org/wp-content/uploads/2024/03/AX1-winter-break-031724_fin.htm'

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
    tables = soup.find_all('table')

    if len(tables) != 2:
        raise ValueError(f"Error: {len(tables)} tables found. There should be at least 3. Verify URL and page to be scraped")

    if tables[1]:
        raceResultTable = tables[1]
        
        # Extract the table rows
        rows = raceResultTable.find_all('tr')

        # Iterate through each row to find each th until a td is found
        attribute_names = ['position', 'class', 'number', 'driver', 'car', 'color', 'run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'total', 'diff']

        # Extract the data from each row and map to attribute names
        table_data = []
        for row in rows:
            cells = row.find_all('td')
            # Ensure the number of cells match the number of attributes
            # If they do not, it's not a data row, so it can be skipped
            if len(cells) == len(attribute_names):
                row_data = {attribute_names[i]: cells[i].text.strip() for i in range(len(attribute_names))}
                table_data.append(row_data) 

        # Convert the table data to JSON format
        table_json = json.dumps(table_data, indent=4)
        
        # Print the JSON data
        print(table_json)
else:
    print("Request was unsuccessful")