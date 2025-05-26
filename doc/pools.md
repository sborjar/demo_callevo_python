# Pools - Import Files
[Back](../README.md#menu)

List of numbers to import to make a call. 
### File to import 
Example
```c
lead_phone,lead_fname,lead_lname,custom,custom1,custom2
7209888027,Constumer1,LName1,AAAAAA1,BBBB1,CCCC1
7209888028,Constumer2,LName2,AAAAAA2,BBBB2,CCCC2
```

### Routes
| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/pools`|`python src/pools/get-pools.py`|
|Get a one |`GET/pools/2012`|`python src/pools/get-pools-id.py`| 
|Create a new |`POST/pool`|`python src/pools/post-pool.py`|  
|Update|`PUT/pool/2012`|`python src/pools/put-pool_id.py`|
|Delete | `DELETE/pool/2012` | `python src/pools/delete-pool-id.py` |
|Start | `POST/start_pool/2012` | `python src/pools/post-start-pool-id.py` |
|Stop| `POST/stop_pool/2012` | `python src/pools/post-stop-pool-id.py` |

### Required data

```json
{
    "poolname": "string",
    "camp_id": "string",
    "allow_duplicate": "boolean n|f|c",
    "randomize": "string y|n",
    "CleanOld": "string 0|1",
    "prefixlen": "string",
    "file_content": "file (formData)"
}
```
**Important Notes** 
To get a `templateid` you must to run first /src/filetemplates/get-template-from-file-header.py, configurando el nombre del archivo a importar
### Required header
```json
{
    "Content-Type": "multipart/form-data",
}
```
