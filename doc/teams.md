# Teams
[Back](../README.MD#menu)

| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/teams`|`python src/teams/get-teams.py`|
|Get a one |`GET/teams/2012`|`python src/teams/get-teams-id.py`| 
|Create a new |`POST/team`|`python src/teams/post-team.py`|  
|Update|`PUT/team/2012`|`python src/teams/put-team.py`|
|Delete | `DELETE/team/2012` | `python src/teams/delete-team.py` |

### Required data
```json
{
    "queueid": "number | -1",
    "name": "string",
    "team_name": "string",
    "musiconhold": "string",
    "queue_member_table": [
        {
            "memberid": "number | new -1",
            "queueid": "number",
            "agentid": "number",
            "queue_name": "string",
            "interface": "string `Agent/<agent_code>`",
            "announce_holdtime": "string",
        }
    ]
}
```
