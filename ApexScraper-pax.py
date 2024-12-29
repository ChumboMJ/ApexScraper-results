import requests
from bs4 import BeautifulSoup
import json

# Script used for scraping pax event data

url = 'https://www.wmclub.org/wp-content/uploads/2024/03/AX1-winter-break-031724_pax.htm'

# Set headers to mimic a browser request
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Use a GET request to retrieve the site page
response = requests.get(url, headers=request_headers)

if response.status_code == 200:
    print("Request was a success!")

    # Parse the HTML Request
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get each of the table on the page
    tables = soup.find_all('table')

    # print the number of tables found
    print("Number of Tables found: " + str(len(tables)))

    if tables[1]:
        paxResultTable = tables[1]

        attribute_names = ['paxPosition', 'classPosition', 'class', 'number', 'driver', 'car', 'total', 'factor', 'paxTime', 'diff', 'fromFirst']

        # Extract the table rows
        rows = paxResultTable.find_all('tr')

        table_data = []
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == len (attribute_names):
                row_data = {attribute_names[i]: cells[i].text.strip() for i in range(len(attribute_names))}
                table_data.append(row_data)

        #Convert the table data to JSON format
        table_json = json.dumps(table_data, indent=4)

        #print the JSON data
        print(table_json)
else:
    print("Request was unsucessful :(")
