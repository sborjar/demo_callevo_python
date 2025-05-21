import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}file_template'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params = {
  "file_template": {
    "id": 0,
    "template_name": "PruebaTemplate"
  },
  "file_template_fields": [
    { "field_name": "Lead Test1","field_source": "lead_phone","field_destination": "lead_phone" },
    { "field_name": "Lead Fname2","field_source": "lead_fname","field_destination": "lead_fname" },
    { "field_name": "Lead Lname2","field_source": "lead_lname","field_destination": "lead_lname" },
    { "field_name": "Custom3","field_source": "custom","field_destination": "custom" },
  ]
}
    
response = requests.post(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles(current_file_name,current_file_method,url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)

