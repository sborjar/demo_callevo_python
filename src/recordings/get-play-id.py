import requests
import sys
import os
import shutil
import wave
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}play/51'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
params = None

folder = "./files"
folder_exists = os.path.exists(folder)
if folder_exists == False:
    os.mkdir(f"{folder}")  

response = requests.get(url, json=params, headers=headers, stream=True)

if response.status_code == 200:
    print('Successful request')
    if response.headers["Accept-Ranges"] == "bytes":
        f = response.headers["Content-Disposition"]
        f = f.replace("attachment;","")
        f = f.replace(" filename=","")
        f = f.replace('"',"")
        
        with wave.open(f'{folder}/{f}', 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2) 
            wf.setframerate(44100)
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    wf.writeframes(chunk)
                
            print(f'File created successfully! {folder}/{f}')
            saveMdFiles(current_file_name,current_file_method,url,headers,params,f'File created successfully! {folder}/{f}')
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)