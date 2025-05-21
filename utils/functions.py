import os

from requests_toolbelt import MultipartEncoder

def getFileNameMethod(file=""):
    only_name = file.split(".")[0]
    method_file_name = only_name.split("-")[0].upper()
    return {"current_file_name":only_name, "current_file_method":method_file_name}

def saveMdFiles(file='', method='', url='', headers={}, params={}, response={}):
    folder = "./results"
    folder_exists = os.path.exists(folder)
    
    if folder_exists == False:
        os.mkdir(f"{folder}")  
    
    name_file = f'{folder}/{file}.md'
    
    if os.path.exists(name_file):
        os.remove(name_file)
    
    color = ""
    if method == "GET":
        color="21577d"
    elif method == "POST":
        color="1c8056"
    elif method == "PUT":
        color="ed8d14"
    elif method == "DELETE":
        color="ad2525"
    
    try:
        file = open(name_file, "a")
        
        file.write(f'\n')
        file.write(f'![](https://img.shields.io/badge/{method}-{color}) ')
        file.write(f'![](https://img.shields.io/badge/{url}-d7d7d7)')
        file.write(f'\n')
        
        file.write(f'### Headers \n')
        file.write(f'```js \n')
        file.write(f'{headers} \n')
        file.write(f'```\n \n')
        
        file.write(f'### Params \n')
        file.write(f'```js \n')
        file.write(f'{params} \n')
        file.write(f'``` \n')
        
        file.write(f'### Response \n')
        file.write(f'```js \n')
        file.write(f'{response} \n')
        file.write(f'``` \n')
        
        file.close()
        print(f"\n!!! The file {name_file} has been created ¡¡¡\n")
    except:
        print("\nError creating the file\n")
    
    

