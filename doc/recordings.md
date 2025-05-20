# Recordings
[Back](../README.MD#menu)


| Description | Route | Command
|-------------|-------|---------|
|Play |`GET/play/id`|`python src/recordings/get-play-id.py`|
|Get a all |`GET/systemrecordings`|`python src/recordings/get-recordings.py`|
|Get a one |`GET/systemrecordings/2012`|`python src/recordings/get-recordings-id.py`| 
|Create a new |`POST/systemrecording`|`python src/recordings/post-recording.py`|  
|Update|`PUT/systemrecording/2012`|`python src/recordings/put-recording-id.py`|
|Delete | `DELETE/systemrecording/2012` | `python src/recordings/delete-recording-id.py` |

### Required data
```json
{
    "recID": "number",
    "recName": "string",
    "filecontent": "file",
}
```
