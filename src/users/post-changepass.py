import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}changepass'

headers = {
    'Content-Type': 'application/json',
}
params = {
    "email": "santiago@callevo.com",
    "newPassword": "Ce21@cAll",
    "oldPassword": "*xUapByNz-"
}

response = requests.post(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles("post-changepass", "POST", url, headers, params, response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)
