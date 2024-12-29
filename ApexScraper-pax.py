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
else:
    print("Request was unsucessful :(")

print(url)
