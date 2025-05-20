# Phones
[Back](../README.MD#menu)

Numbers or phones numbers.

| Description | Route | Command
|-------------|-------|---------|
|Get a all |`GET/phones`|`python src/phones/get-phones.py`|
|Get a one |`GET/phones/2012`|`python src/phones/get-phones-id.py`| 
|Create a new |`POST/phone`|`python src/phones/post-phone.py`|  
|Update|`PUT/phone/2012`|`python src/phones/put-phone.py`|
|Delete | `DELETE/phone/2012` | `python src/phones/delete-phone.py` |

### Required data
```json
{
  "active": "number 1|0",
  "description": "string",
  "phone": "string"
}
```
