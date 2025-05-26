# Tenants

[Back](../README.md#menu)


| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/tenants`|`python src/tenants/get-tenants.py`|
|Get a one |`GET/tenants/2012`|`python src/tenants/get-tenants-id.py`| 
|Update|`PUT/tenant/2012`|`python src/tenants/put-tenant.py`|

### Required data
```json
{
    "activate_tenant": "string",
    "address": "string",
    "email" : "string",
    "camp_type": "string",
    "defaultcalleridgroup": "number",
    "inbound_number": "string",
    "name": "string",
    "selectcmp": "number",
    "leadtype": "string",
    "timeid": "number",
    "timeused": "number",
    "usedispopt": "number"
}
```