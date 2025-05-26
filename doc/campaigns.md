# Campaigns

[Back](../README.MD#menu)


| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/campaigns`|`python src/campaigns/get-campaigns.py`|
|Get a one |`GET/campaigns/2012`|`python src/campaigns/get-campaigns-id.py`| 
|Create a new |`POST/campaign`|`python src/campaigns/post-campaign.py`|  
|Update|`PUT/campaign/2012`|`python src/campaigns/put-campaign.py`|
|Delete | `DELETE/campaign/2012` | `python src/campaigns/delete-campaign.py` |

### Required data
```json
{
    "camp_id": "number",
    "camp_name": "string",
    "camp_description": "string",
    "camp_type": "string",
    "dropcb": "string", 
    "timezones": "string",
}
```
When the operation is new, the `camp_id` can be 0 or deleted.<br>
The values for the `dropcb` and `timezones` fields are `y` or `n`.
### Campaign Type (`camp_type`)
```js
CL - Click to Dial
MA - Manual
IN - Inbound
AC - Agent to Agent
P1 - Messaging
P2 - Predictive
P3 - Preview
```
### More options
```json
{
    "camp_id": "number",
    "camp_name": "string",
    "camp_description": "string",
    "camp_type": "string",
    "active": "string",
    "allow_inbound": "string",
    "callDataN": "string",
    "calldataF": "string",
    "calldataS": "string",
    "customfield": "string",
    "customlabel": "string",
    "campaign_schedule": {
        "friday_active": "number",
        "friday_start": "hh:mm:ss",
        "friday_stop": "hh:mm:ss",
        "monday_active": "number",
        "monday_start": "hh:mm:ss",
        "monday_stop": "hh:mm:ss",
        "saturday_active": "number",
        "saturday_start": "hh:mm:ss",
        "saturday_stop": "hh:mm:ss",
        "schedule_id": "number",
        "sunday_active": "number",
        "sunday_start": "hh:mm:ss",
        "sunday_stop": "hh:mm:ss",
        "thursday_active": "number",
        "thursday_start": "hh:mm:ss",
        "thursday_stop": "hh:mm:ss",
        "tuesday_active": "number",
        "tuesday_start": "hh:mm:ss",
        "tuesday_stop": "hh:mm:ss",
        "updated_at": "hh:mm:ss",
        "wednesday_active": "number",
        "wednesday_start": "hh:mm:ss",
        "wednesday_stop": "hh:mm:ss"
    },
    "defaultdisp": "number",
    "dispositions": [
        {
        "campdisp": [
            {
            "camp_id": "number"
            }
        ],
        "contact": "string",
        "crcid": "number",
        "dispcode": "string",
        "dispdesc": "string",
        "dispid": "number",
        "dnc": "string",
        "enabled": "string",
        "finalcrc": "string",
        "presentation": "string",
        "recall": "string",
        "recallscale": "number",
        "revenue": "number",
        "seconds": "number",
        "success": "string"
        }
    ],
    "dropcb": "string",
    "forcedisposition": "string",
    "inbound_number": "string",
    "linesdialed": "number",
    "notifyholding": "string",
    "phoneID": "number",
    "posturlcall": "string",
    "qcenabled": "string",
    "qcurl": "string",
    "queue_name": "string",
    "ratio": "string",
    "showcustomfield": "string",
    "showdisp": "string",
    "smsnumber": "string",
    "startdialing": "string",
    "status": "number",
    "timezones": "string",
    "urlcall": "string",
    "usecampdncfrom": "string",
    "usecmpdnc": "string",
    "usedncglobal": "string"
}
```