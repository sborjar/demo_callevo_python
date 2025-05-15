import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = f'{os.getenv("API_PATH")}appversion?app=agent'

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, DELETE',
    'Access-Control-Allow-Headers': 'Accept,Accept-Language,Content-Language,Content-Type',
    'Access-Control-Expose-Headers': 'Content-Length,Content-Range',
}
response = requests.get(url)

if response.status_code == 200:
    print('Successful request')
    print('Response:', response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details', response)