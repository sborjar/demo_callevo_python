import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}phone/17992'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params = {
  "active": 1,
  "description": "Desde python Test modificado",
  "phone": "593995918919"
}
response = requests.put(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles("put-phones","PUT",url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)
