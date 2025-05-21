import base64
import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

url = f'{os.getenv("API_PATH")}make_template'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params =  None

file_name = "import_pool.csv"
file_path = f'{sys.path[0]}files/{file_name}'

if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
    
    f = open(file_path)
    file_header = f.readline()
    file_header = file_header.replace('\n','')
    file_header = file_header.strip()
    params = {"file_header": file_header}
    
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
else:
    print(f"File '{file_path}' does not exist.")






