# CallEvo Api RestFul Demo

Developer Tools

![](https://img.shields.io/badge/Python-3.12-blue) 

## Installation
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
### How to use this guide

First you must open the Api documentation. [`http://616262.ip.hamvoip.org:8082/doc/index.html#/`](http://616262.ip.hamvoip.org:8082/doc/index.html#/)

In the documentation it indicates how the path is defined and the requirements it has.

For this demo each path can be found in the `./src/` folder and is subdivided in groups, and they are the same as in the documentation. Ex: If the route says GET/appversion inside General Routes then the corresponding demo file is in `./src/general/get-appversion.py` or `./src/general/public/get-node_list`.

![image](./images/api-doc.jpg)

# Important
1. The following files are important for the correct functioning of the demo:
```
.env -> Environment Variables
```
```
API_PATH=http://616262.ip.hamvoip.org:8082/api/v2/
APP_TOKEN=<token>
```
2. Each file has a working code example that works without problems. 
3. When the file is run, the result is saved in the `results` folder.

# Execute Demo

1. You must to select a route and group: Ex: `General/GET/appversion`
2. Run
```
python /src/general/get-appversion.py
```
3. Response
```js
Successful request
Response: {'action': 'appversion', 'data': {'appversion': 'v1.250'}, 'id': '', 'message': '', 'result': 'OK'}
```
# Check if the api is healthy
```
python /src/general/get-health.py 
```
Result
```js
Successful request
Data: {'action': 'checkhealth', 'id': '', 'message': 'Healthy', 'result': 'OK'}
```

# What routes should I follow to be able to dial 

To start to dial you must following some steps:
1. Callevo Administration gives you a token, you must paste in a .env file
1. [Manage Users](/doc/users.md)
1. [Manage Agents](/doc/agents.md)
1. [Manage Teams (projets groups)](/doc/teams.md)
1. [Numbers / Phones](/doc/phones.md)
1. [Caller ID Groups](/doc/calleridgroups.md)
1. [Manage Campaigns (Projects)](/doc/campaigns.md)
1. [File Templates](/doc/pools.md)
1. [Import files (Pools)](/doc/pools.md)
1. TimesZones
1. Recordings

# More examples

### Users

| Description | Route | Command
|-------------|-------|---------|
|Get a list of my tenant's users|`GET/users`|`python src/users/get-users.py`|
|Get a specific user|`GET/users/2012`|`python src/users/get-users-id.py`| 
|Create a new user|`POST/user`|`python src/users/post-user.py`|  
|Update a user|`PUT/user/2012`|`python src/users/put-user.py`|
|Delete a user | `DELETE/user/2012` | `python src/users/delete-user.py` |


