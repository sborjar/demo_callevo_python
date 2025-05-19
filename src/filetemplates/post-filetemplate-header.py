import base64
import requests
import sys
import os
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

url = f'{os.getenv("API_PATH")}make_templates'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}

params =  None

def getTemplate(file_header):
    file_header = file_header.replace('\n','')
    file_header = file_header.strip()
    print(file_header)

    # Convert base64
    header_encode = file_header.encode("ascii")
    base64_bytes = base64.b64encode(header_encode)
    base64_string = base64_bytes.decode("ascii")

    params = {"file_header": base64_string}
    response = requests.post(url, json=params, headers=headers)

    if response.status_code == 200:
        print('Successful request')
        print('Data:', response.json())
        saveMdFiles("post-templates-header","POST",url,headers,params,response.json())
    else:
        print('Error in the request, details:', response.text)
        print('Details:')
        print('Status Code:', response.status_code)
        print(response)


if __name__ == "__main__":
    file_path = f'{sys.path[0]}files/import_file.csv'

    if os.path.exists(file_path):
        print(f"File '{file_path}' exists.")
        f = open(file_path)
        file_header = f.readline()
        getTemplate(file_header=file_header)
    else:
        print(f"File '{file_path}' does not exist.")






   