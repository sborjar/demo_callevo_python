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
<a id="menu"></a>
To start to dial you must following some steps:
|Step|Description|Actions|Command to run|
|---|---|---|---|
|1|Callevo Administration gives you a token which you must paste into an environment variable file in the .env file. | [+Info](/doc/create_environment_file.md) ||
|2|Create a users (agents/clickers) and obtain the `userid` <br>Ex: {..."message": 12} from response|[+Info](/doc/users.md)<br>[Edit](/src/users/post-user.py)|python src/users/post-user.py|
|3|Collect user data by getting the `agent_code` and `agentid` field|[Edit](src/users/get-users-id.py)|python src/users/get-users-id.py|
|4|Create a team and paste the `agent_code` into the interface field => "Agent/<agent_code>"|[+Info](/doc/teams.md)<br>[Edit](/src/teams/post-team.py)|python src/teams/post-team.py|
|5|Collect team data by queue_id to get the `name` field, <br> Ex: `{..name: "q282fpqah33qky3s8egq90"}`|[Edit](/src/teams/get-teams-id.py)|python src/teams/get-teams-id.py|
|6|Create a phone and obtain the `phoneid` from response {message: '1852'}|[+Info](/doc/phones.md)<br>[Edit](/src/phones/post-phone.py)|python src/phones/post-phone.py|
|7|Create a caller ID group with the obtained phoneIDs. After executing you can get the `groupid` <br> Ex: {'message': '315'}|[+Info](/doc/calleridgroups.md)<br>[Edit](src/caller-id-groups/post-caller-id-group.py)|python src/caller-id-groups/post-caller-id-group.py|
|8|Import a recording and get the `recID` of the response {message: '100'}|[+Info](/doc/recordings.md)<br>[Edit](/src/recordings/post-systemrecording.py)|python src/recordings/post-systemrecording.py|
|9|Create a campaign and obtain the `camp_id`.<br> Optional: you can complement the campaign information by filling the fields with data obtained in previous routes such as: groupid, name (team name), initialrecordID/finalrecordID with the recID|[+Info](/doc/campaigns.md)<br>[Edit](/src/campaigns/post-campaign.py)|python src/campaigns/post-campaign.py|
|10|Upload the file containing the numbers to make the calls.<br>You must paste the file in the `files` folder.|[+Info](/doc/pools.md)<br>[Edit](/src/pools/post-pool.py) |python src/pools/post-pool.py|
|11|Import data from file uploaded.<br>You can see the result with the following information: `{'dedup': 0, 'elegibles': 0, 'error': 0, 'merge': 1499, 'scrub': 0, 'upload': 1499}` |[Edit](/src/pools/post-file-import-id.py)|python src/pools/post-file-import-id.py
|12|Start file imported|[Edit](/src/pools/post-start-pool-id.py)|python src/pools/post-start-pool-id.py
|13|Start a campaign


# Important route management documentation
1. [Users](/doc/users.md)
1. [Teams (projets groups)](/doc/teams.md)
1. [Numbers / Phones](/doc/phones.md)
1. [Caller ID Groups](/doc/calleridgroups.md)
1. [Campaigns (Projects)](/doc/campaigns.md)
1. [File Templates](/doc/filetemplates.md)
1. [Import files (Pools)](/doc/pools.md)
1. [Recordings](/doc/recordings.md)
1. [Tenants](/doc/tenants.md)
1. TimesZones

# More examples

### Users

| Description | Route | Command
|-------------|-------|---------|
|Get a list of my tenant's users|`GET/users`|`python src/users/get-users.py`|
|Get a specific user|`GET/users/2012`|`python src/users/get-users-id.py`| 
|Create a new user|`POST/user`|`python src/users/post-user.py`|  
|Update a user|`PUT/user/2012`|`python src/users/put-user-id.py`|
|Delete a user | `DELETE/user/2012` | `python src/users/delete-user-id.py` |

# Testing Example
*Step 1*. ok, I created the .env file and put the token inside.

*Step 2*. Create a users<br>
```c
    python src/users/post-user.py
```
```json
    {, 'message': '15315',} --> userid = 15315
    {, 'message': '15313',} --> userid = 15313
    {, 'message': '15314',} --> userid = 15314
```
*Step 3*. Collect a users data
```c
    python src/users/get-users-id.py
```
```c
    15315   agent_code=u282xdaw7ahwzfz5gsht    agentid=15337
    15313   agent_code=u282ms5xpeg5m696zckb    agentid=15338 
    15314   agent_code=u2822htb7mp0d8rnehrd    agentid=15339
```
*Step4*. Create a team
```c
    python src/teams/post-team.py
```
```c
    queue_id = 10211
```
*Step 5*. Collect a team data
```c
    python src/teams/get-teams-id.py
```
```c
    name = q282ubzotmgr12bss9zb
```
*Step 6*. Create phones
```c
    python src/phones/post-phone.py
```
```c
    phoneid = 18003
```
*Step 7*. Create CallerIDGroup
```c
    python src/caller-id-groups/post-caller-id-group.py
```
```c
    groupid = 316
```
*Step 8*. Import a recording
```c
   python src/recordings/post-systemrecording.py 
```
```c
    recID = 37
```
*Step 9*. Create a campaign 
```c
    python src/campaigns/post-campaign.py
```
```c
    camp_id = 1800
```
*Step 10*. Upload a file to import
```c
    python src/pools/post-pool.py
```
```c
    poolid = 2621
```
*Step 11*. Import file uploaded
```c
    python src/pools/post-file-import-id.py
```
```c
    {'dedup': 0, 'elegibles': 0, 'error': 0, 'merge': 1499, 'scrub': 0, 'upload': 1499}
```
*Step 12*. Start file
```c
    python src/pools/post-start-pool-id.py
```
```c
    {'action': 'start_pool', 'data': {}, 'id': '', 'message': '', 'result': 'OK'}
```

