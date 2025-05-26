# Caller ID Groups
[Back](../README.md#menu)

Numbers or caller id groups numbers.

| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/caller_id_groups`|`python src/caller-id-groups/get-caller-id-groups.py`|
|Get a one |`GET/caller_id_groups/2012`|`python src/caller-id-groups/get-caller-id-groups-id.py`| 
|Create a new |`POST/caller_id_group`|`python src/caller-id-groups/post-caller-id-group.py`|  
|Update|`PUT/caller_id_group/2012`|`python src/caller-id-groups/put-caller-id-group_id.py`|
|Delete | `DELETE/caller_id_group/2012` | `python src/caller-id-groups/delete-caller-id-group-id.py` |

### Required data
```json
{
    "groupid": "number",
    "group_name": "string",
    "camp_id": "number",
    "phone": [
        {
            "phoneid": "number"
        }
    ]
}
```
When the operation is new, the `groupid` can be 0 or deleted.