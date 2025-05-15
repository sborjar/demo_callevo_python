import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}authlogin'

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, DELETE',
    'Access-Control-Allow-Headers': 'Accept,Accept-Language,Content-Language,Content-Type',
    'Access-Control-Expose-Headers': 'Content-Length,Content-Range',
}

params = {
    "email": os.getenv("APP_USER"),
    "password": os.getenv("APP_PASS"),
    # "usertype": ["27"]
}

# User type can be Agent - 27 / Clicker - 30 or release if is admin

response = requests.post(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles("post-authlogin","POST",url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)