# File Templates
[Back](../README.md#menu)

Numbers or caller id groups numbers.

| Description | Route | Command
|-------------|-------|---------|
|Get all |`GET/file_templates`|`python src/filetemplates/get-filetemplates.py`|
|Get one |`GET/file_templates/823`|`python src/filetemplates/get-filetemplates-id.py`|
|Get one from header|`GET/file_templates/2012`|`python src/filetemplates/get-filetemplates-id.py`| 
|New from json |`POST/file_template`|`python src/filetemplates/post-filetemplate-json.py`|  
|New from header |`POST/make_template`|`python src/filetemplates/post-filetemplate-header.py`|  
|Duplicate |`POST/duplicate_template/823`|`python src/filetemplates/post-duplciate-template-id.py`|  
|Update|`PUT/file_template/2012`|`python src/filetemplates/put-filetemplate_id.py`|
|Delete | `DELETE/file_template/2012` | `python src/filetemplates/delete-filetemplate-id.py` |

### Required data
```json
{
    "file_template": {
        "id": "number",
        "template_name": "string"
    },
    "file_template_fields": [
        {
            "field_destination": "string",
            "field_name": "string",
            "field_source": "string"
        }
    ]
}
```
When the operation is new, the `id` can be 0 or deleted.

