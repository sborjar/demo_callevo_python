import base64
import json
import requests
import sys
import os
sys.path.insert(0, os.getcwd())
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

url = f'{os.getenv("API_PATH")}file_templates'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}

params =  None


def getTemplate(file_header):
    file_header = file_header.replace('\n','')
    file_header = file_header.strip()

    # Convert base64
    header_encode = file_header.encode("ascii")
    base64_bytes = base64.b64encode(header_encode)
    base64_string = base64_bytes.decode("ascii")

    params = {"file_header": base64_string}
    try:
        response = requests.get(url, json=params, headers=headers)
    except Exception as error:
        print(error)
        sys.exit(1)
    
    if response.status_code == 200:
        print('Successful request')
        print('Data:', response.json())
        saveMdFiles(current_file_name,current_file_method,url,headers,params,response.json())
        
        # Get an id as templateid for pools when importing a new file POST/pool
        data = response.json().get("data")
        file_templates = data.get("file_templates")
        templateID = file_templates[0]["id"]
        print("This ID will be useful when importing a new file into pools, templateID=", templateID)
        
    else:
        print('Error in the request, details:', response.text)
        print('Details:')
        print('Status Code:', response.status_code)
        print(response)


if __name__ == "__main__":
    # Process of loadign a file to obtain a header structure
    file_path = f'{sys.path[0]}/files/List_MyTest.csv'

    if os.path.exists(file_path):
        print(f"File '{file_path}' exists.")
        f = open(file_path)
        file_header = f.readline()
        getTemplate(file_header=file_header)
    else:
        print(f"File '{file_path}' does not exist.")






   