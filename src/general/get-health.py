import requests
from dotenv import load_dotenv
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
import os

load_dotenv()

url = f'{os.getenv("API_PATH")}public/health'

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, DELETE',
    'Access-Control-Allow-Headers': 'Accept,Accept-Language,Content-Language,Content-Type',
    'Access-Control-Expose-Headers': 'Content-Length,Content-Range',
}

response = requests.get(url,None,headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles(current_file_name,current_file_method,url,headers,None,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)