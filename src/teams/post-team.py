import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}team'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params =  {
    "queueid": -1,
    "record": { 
        "name": "TeamDemo",
        "team_name": "TeamDemo",
     },
    "queue_member_table": [
        {
            "agentid": 34,    
            "queue_name": "TeamDemo",
            "interface": "Agent/u282dxqb8two6vmoqhdw",
        },
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