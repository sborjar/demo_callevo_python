import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = f'{os.getenv("API_PATH")}authlogin'

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, DELETE',
    'Access-Control-Allow-Headers': 'Accept,Accept-Language,Content-Language,Content-Type',
    'Access-Control-Expose-Headers': 'Content-Length,Content-Range',
}

data = {
    "email": os.getenv("APP_USER"),
    "password": os.getenv("APP_PASS"),
    "usertype": ["27"]
}

# User type can be Agent - 27 / Clicker - 30 or release if is admin

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)