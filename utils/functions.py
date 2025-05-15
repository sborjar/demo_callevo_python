import os

def saveMdFiles(file='', method='', url='', headers={}, params={}, response={}):
    folder = "./results"
    if os.path.exists(folder):
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
        except:
            print("Error with create the file")
        
        print(f"\n!!! The file {name_file} has been created ¡¡¡\n")
    else:
        print(f"{folder} not exist")
    

