import requests
import sys
import os
sys.path.insert(0, os.getcwd())
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
    "record": { 
        "name": "TeamDemo2",
        "team_name": "TeamDemo2",
     },
    "queue_member_table": [
        {
            "agentid": 15337,    
            "queue_name": "TeamDemo2",
            "interface": "Agent/u282xdaw7ahwzfz5gsht",
        },
        {
            "agentid": 15338,    
            "queue_name": "TeamDemo2",
            "interface": "Agent/u282ms5xpeg5m696zckb",
        },
        {
            "agentid": 15339,    
            "queue_name": "TeamDemo2",
            "interface": "Agent/u2822htb7mp0d8rnehrd",
        },
       
    ]
}

try:
    response = requests.post(url, json=params, headers=headers)
except Exception as error:
    print(error)
    sys.exit(1)
    
if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles(current_file_name,current_file_method,url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)