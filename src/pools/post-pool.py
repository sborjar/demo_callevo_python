import requests
import sys
import os
import mimetypes
import uuid
from requests_toolbelt import MultipartEncoder
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}pool'
boundary = str(uuid.uuid4())
headers = {
    # 'Content-Type': f"multipart/form-data; boundary={boundary}",
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}

params = None
file_name = "List_MyTest.csv"
file_path = f'{sys.path[0]}/files/{file_name}'
if os.path.exists(file_path):
    # try:
    #     with open(file_path, 'rb') as file:
    #         file_content = file.read()
    # except FileNotFoundError:
    #     print(f"Error: File not found at {file_path}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
        
    # mime_type, encoding = mimetypes.guess_type(file_path)
    # print(mime_type)
    # text_content = file_content.decode('utf-8')
    # print(text_content)
    # print(file_content)
    params = {
        "poolname": "Example Uno",
        "file_content": (file_name, open(file_path, 'rb'), 'audio/wave'),
        "camp_id": "2",
        "allow_duplicate": "n",
        "randomize": "y",
        "CleanOld": "0",
        "prefixlen": "3",
    }
    
    file_encoder =  MultipartEncoder(params)
    print(file_encoder.to_string())
    
    headers["Content-Type"] = file_encoder.content_type
    
    print(headers)
        
    response = requests.post(url, data=file_encoder, headers=headers)

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
    
    