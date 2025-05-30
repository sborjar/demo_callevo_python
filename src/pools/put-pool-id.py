import requests
import sys
import os
import mimetypes
import uuid
from requests_toolbelt import MultipartEncoder
sys.path.insert(0, os.getcwd())
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}pool/1369'
boundary = str(uuid.uuid4())
headers = {
    # 'Content-Type': f"multipart/form-data; boundary={boundary}",
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}

params = {
    "poolname": "Update List_Phones.txt ",
    "camp_id": "2",
    "allow_duplicate": "n",
    "randomize": "y",
    "CleanOld": "0",
    "prefixlen": "3",
}

# file_encoder =  MultipartEncoder(params)
# print(file_encoder.to_string())
# headers["Content-Type"] = file_encoder.content_type
# print(headers)
    
try:
    response = requests.put(url, json=params, headers=headers)
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
