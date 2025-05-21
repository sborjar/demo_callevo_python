import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}campaign'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params = {
    "camp_id": -1,
    "camp_name": "democamp",
    "camp_description": "Demo Campaign",
    "camp_type": "CL",
    "dropcb": "y",
    "timezones": "n",
    "groupid": 315,
    "didrotation": 2,
    "queue_name": "q282fpqahtqkyc8egq90",
    "recordings": 1,
    "initialrecordID": 36,
    "finalrecordID": 36,
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