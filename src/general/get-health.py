import requests
import sys
import os
sys.path.insert(0, os.getcwd())
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

# Validations
if os.getenv("API_PATH") == None:
    print("Fatal!!!: No .env file exists. See README.MD for information on how to create an environment file.")
else:
    url = f'{os.getenv("API_PATH")}public/health'
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, DELETE',
        'Access-Control-Allow-Headers': 'Accept,Accept-Language,Content-Language,Content-Type',
        'Access-Control-Expose-Headers': 'Content-Length,Content-Range',
    }

    try:
        response = requests.get(url,None,headers=headers)
    except Exception as error:
        print(error)
        sys.exit(1)

    if response.status_code == 200:
        print('Successful request')
        print('Data:', response.json())
        saveMdFiles(current_file_name,current_file_method,url,headers,None,response.json())
    else:
        print('Error in the request, details:', response.text)
        print('Details:')
        print('Status Code:', response.status_code)
        print(response)