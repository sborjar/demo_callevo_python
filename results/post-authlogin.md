``` 
POST | http://616262.ip.hamvoip.org:8082/api/v2/authlogin 
``` 
### Headers 
```js 
{'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, DELETE', 'Access-Control-Allow-Headers': 'Accept,Accept-Language,Content-Language,Content-Type', 'Access-Control-Expose-Headers': 'Content-Length,Content-Range'} 
```
 
### Params 
```js 
{'email': 'santiago@callevo.com', 'password': 'Ce21@cAll', 'usertype': ['27']} 
``` 
### Response 
```js 
{'action': 'authlogin', 'data': {'authlogin': [{'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'Default Tenant', 'tenantid': 25, 'userid': 372, 'username': 'u2514987d84ee12cc9a3', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'Tenant Rick', 'tenantid': 86, 'userid': 373, 'username': 'u86008db1af91cf7d4e7', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'Mid West Cash Offer', 'tenantid': 139, 'userid': 894, 'username': 'u139533badbf98ba6373', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'MVP', 'tenantid': 204, 'userid': 1984, 'username': 'u2047c6551420038c44a', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'saultenant', 'tenantid': 212, 'userid': 2014, 'username': 'u2120602d013ce0ceaa2', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'SEIUCC', 'tenantid': 140, 'userid': 2017, 'username': 'u1406d53b29c122754af', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'JJSC Tenant test', 'tenantid': 138, 'userid': 2018, 'username': 'u138671bc38071e2e900', 'usertype': 27, 'usertype_description': 'Agent'}, {'email': 'santiago@callevo.com', 'pass': 'Ce21@cAll', 'tenant_name': 'ACCE', 'tenantid': 211, 'userid': 3253, 'username': 'u211d3c88453e119b550', 'usertype': 27, 'usertype_description': 'Agent'}]}, 'id': '', 'message': '', 'result': 'OK'} 
``` 
