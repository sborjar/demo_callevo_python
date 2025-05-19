# Pools
### Import Files
[Back](../README.MD)

Numbers or caller id groups numbers.

| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/pools`|`python src/pools/get-pools.py`|
|Get a one |`GET/pools/2012`|`python src/pools/get-pools-id.py`| 
|Create a new |`POST/pool`|`python src/pools/post-pool.py`|  
|Update|`PUT/pool/2012`|`python src/pools/put-pool_id.py`|
|Delete | `DELETE/pool/2012` | `python src/pools/delete-pool-id.py` |

### Required data

```json
{
    "poolname": "string",
    "camp_id": "number",
    "allow_duplicate": "boolean n|f|c",
    "randomize": "string y|n",
    "CleanOld": "number 0|1",
    "prefixlen": "number",
    "templateid": "number (see Important Notes) ",
    "file_content": "file (fromData)"
}
```
**Important Notes** 
To get a `templateid` you must to run first /src/filetemplates/get-template-from-file-header.py, configurando el nombre del archivo a importar
### Required header
```json
{
    "mimeType": "multipart/form-data",
}
```

