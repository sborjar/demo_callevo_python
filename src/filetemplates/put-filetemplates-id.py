import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}file_template/823'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params = {
  "file_template": {
    "id": 823,
    "template_name": "List_MyTest.txt-templates2"
  },
  "file_template_fields": [
    { "field_name": "Lead Pepe","field_source": "lead_phone","field_destination": "lead_phone" },
    { "field_name": "Lead Fname","field_source": "lead_fname","field_destination": "lead_fname" },
    { "field_name": "Lead Lname","field_source": "lead_lname","field_destination": "lead_lname" },
    { "field_name": "Custom","field_source": "custom","field_destination": "custom" },
  ]
}
    
response = requests.put(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles("put-templates-id","PUT",url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)

