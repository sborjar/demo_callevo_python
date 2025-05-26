import requests
import sys
import os
sys.path.insert(0, os.getcwd())
from utils.functions import saveMdFiles,getFileNameMethod
current_file_name, current_file_method = getFileNameMethod(__file__)
from dotenv import load_dotenv
load_dotenv()

url = f'{os.getenv("API_PATH")}campaign/1796'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("APP_TOKEN")}',
}
# params = {
#     "camp_name": "TestSBMesDeMayo",
# }
params = {
    "camp_name": "Campaña de prueba",
    "queue_name": "q25u56emzwqnqkslstk8",
}
response = requests.put(url, json=params, headers=headers)

if response.status_code == 200:
    print('Successful request')
    print('Data:', response.json())
    saveMdFiles(current_file_name,current_file_method,url,headers,params,response.json())
else:
    print('Error in the request, details:', response.text)
    print('Details:')
    print('Status Code:', response.status_code)
    print(response)