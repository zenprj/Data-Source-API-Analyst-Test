import requests
import json
import time
from pprint import pprint

#Set up token and headers
TOKEN = "your-token"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def test_authentication():
    """Function to verify authentication"""
    url = "https://api.github.com/user"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        print("Authentication successful!")
    else:
        print(f"Authentication failed: {response.status_code}")
        pprint(response.json())

test_authentication()