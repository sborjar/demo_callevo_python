import requests
import sys
import os

from requests_toolbelt import MultipartEncoder
sys.path.insert(0, f'/workspaces/democallevo/')
from utils.functions import saveMdFiles
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}systemrecording'

headers = { 'Authorization': f'Bearer {os.getenv("APP_TOKEN")}' }
params = { "recName": "Example Uno" }

file_name = "testsantiago.wav"
file_path = f'{sys.path[0]}/files/{file_name}'

def uploadFile():
    with open(file_path, 'rb') as wav_file:
        fields = {'filecontent': (file_path, wav_file, 'audio/wave')}
        if params:
            fields.update(params)

        encoder = MultipartEncoder(fields=fields)
        headers['Content-Type'] =  encoder.content_type
        
        response = requests.post(url, data=encoder, headers=headers)
    return response

if __name__ == "__main__":
    if os.path.exists(file_path):
        response = uploadFile()
        if response.status_code == 200:
            print('Successful request')
            print('Data:', response.json())
            saveMdFiles("post-systemrecording","POST",url,headers,params,response.json())
        else:
            print('Error in the request, details:', response.text)
            print('Details:')
            print('Status Code:', response.status_code)
            print(response)
    else:
        print(f"File '{file_path}' does not exist.")
