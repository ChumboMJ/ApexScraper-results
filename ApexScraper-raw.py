import requests
from bs4 import BeautifulSoup
import json

# Script used for scraping event data for raw times

url = 'https://www.wmclub.org/wp-content/uploads/2024/03/AX1-winter-break-031724_raw.htm'

# Set headers to mimic a browser request
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Use a GET request to retrieve the site page
response = requests.get(url, headers=request_headers)

# Check if the request was a success
if response.status_code == 200:
    print("Request was a success!")

    # Parse the HTML Request
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get each of the table on the page
    tables = soup.find_all('table')

    # Print the number of tables on the page
    print('number of tables found: ' + str(len(tables)))

    if tables[1]:
        rawResultTable = tables[1]

        attribute_names = ['rawPosition', 'classPosition', 'class', 'number', 'driver', 'car', 'rawTime', 'diff', 'fromFirst']

        # Extract the table rows
        rows = rawResultTable.find_all('tr')

        table_data = []
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == len(attribute_names):
                row_data = {attribute_names[i]: cells[i].text.strip() for i in range(len(attribute_names))}
                table_data.append(row_data)

        table_json = json.dumps(table_data, indent=4)

        print(table_json)
else:
    print("Request was unsuccessful")