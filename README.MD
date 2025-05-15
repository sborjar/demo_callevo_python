# CallEvo Api RestFul Demo

Developer Tools

![](https://img.shields.io/badge/Python-3.12-blue) 

Optional 

![](https://img.shields.io/badge/Docker-4.41.2-red) 

c## Installation
### Option 1. Install without Docker
```c
pip install --upgrade pip
pip install -r requirements.txt
```
### Option 2. Install without Docker but with python environment
```c
pyhton -m venv venv 
./venv/Script/activate
pip install --upgrade pip
pip install -r requirements.txt
```
### Option 3. Install with Docker support
You need to install a vscode extension called: Dev Container
```c
Ctrl + Shift + p 
Select a `Dev Containers: Reopen in Container`
```
# Api Documentation
`http://616262.ip.hamvoip.org:8082/doc/index.html#/`

# How to use this guide

First you must open the Api documentation.

In the documentation it indicates how the path is defined and the requirements it has.

For this demo each path can be found in the `./src/` folder and is subdivided in groups, and they are the same as in the documentation. Ex: If the route says GET/appversion inside General Routes then the corresponding demo file is in `./src/general/get-appversion.py` or `./src/general/public/get-node_list`.

![image](./images/api-doc.jpg)

# Important
The following files are important for the correct functioning of the demo:
```c
.env -> Environment Variables
```
# Execute Demo

1. You must to select a route and group: Ex: General/GET/appversion
2. To execute
```c
python ./src/general/get-appversion.py
```
3. Get the response
```c
Successful request
Response: {'action': 'appversion', 'data': {'appversion': 'v1.250'}, 'id': '', 'message': '', 'result': 'OK'}
```
# Check if the api is healthy
```c
python ./src/general/get-health.py 
```
Result
```c
Successful request
Data: {'action': 'checkhealth', 'id': '', 'message': 'Healthy', 'result': 'OK'}
```