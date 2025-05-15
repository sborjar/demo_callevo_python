# CallEvo Api RestFul Demo

Developer Tools

![](https://img.shields.io/badge/Python-3.12-blue) 

c## Installation
### Option 1. Install 
```
pip install --upgrade pip
pip install -r requirements.txt
```
### Option 2. Install with python environment
```
pyhton -m venv venv 
./venv/Script/activate
pip install --upgrade pip
pip install -r requirements.txt
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
```
.env -> Environment Variables
```
.env
```
API_PATH=http://616262.ip.hamvoip.org:8082/api/v2/
APP_USER=<email>
APP_PASS=<password>
APP_TOKEN=
```
# Execute Demo

1. You must to select a route and group: Ex: General/GET/appversion
2. To execute
```
python ./src/general/get-appversion.py
```
3. Get the response
```
Successful request
Response: {'action': 'appversion', 'data': {'appversion': 'v1.250'}, 'id': '', 'message': '', 'result': 'OK'}
```
# Check if the api is healthy
```
python ./src/general/get-health.py 
```
Result
```
Successful request
Data: {'action': 'checkhealth', 'id': '', 'message': 'Healthy', 'result': 'OK'}
```

# What routes should I follow to be able to dial 

To start to dial you must following some steps:
1. [Get a token from user and password](/doc/doc_get_token_from_user_pass.md)
1. [Manage a teams (projets groups)](/doc/teams.md)
1. [Manage an Users](/doc/users.md)
1. Numbers
1. Recordings
1. Projects
1. TimesZones