import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}team/10191'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params =  {
    "queueid": 10192,
    "record": { 
        "name": "Tranzas Modificado",
        "team_name": "Tranzas Modificado",
     },
    "queue_member_table": [
        {
            "agentid": 34,
            "queue_name": "Tranzas Modificado",
            "interface": "Agent/u257937e6609facda319",
        },
        {
            "agentid": 38,
            "queue_name": "Tranzas Modificado",
            "interface": "Agent/u25a3f219d835221a0bf",
        },
        {
            "agentid": 39,
            "queue_name": "Tranzas Modificado",
            "interface": "Agent/u2532da6ac36cbb4389c",
        },
    ]
}

response = requests.put(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles("put-team-id","PUT",url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)