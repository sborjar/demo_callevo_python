import os

from requests_toolbelt import MultipartEncoder

def saveMdFiles(file='', method='', url='', headers={}, params={}, response={}):
    folder = "./results"
    folder_exists = os.path.exists(folder)
    
    if folder_exists == False:
        os.mkdir(f"{folder}")  
    
    name_file = f'{folder}/{file}.md'
    
    if os.path.exists(name_file):
        os.remove(name_file)
    
    print(f"\nCreating a file {name_file} \n")
    
    try:
        file = open(name_file, "a")
        
        file.write(f'``` \n')
        file.write(f'{method} | {url} \n')
        file.write(f'``` \n')
        
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
    
    

