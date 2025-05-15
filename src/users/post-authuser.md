# Auth User 

### Requeriments
1. You must to run first POST/authlogin
2. Select a userid. Each userid has an associated tenant and a user type admin/agent/clicker.
3. Replace usertype in the json data for userid
4. The main data that you mus use in all system is a token. it needs add to Authorization type Bearer, ex:
```c
headers: {
    ...,
    "Authorization": "Bearer eyJraWQiOiJnVTVhMEUxUW95bGVtaFwvWE8xc.....1cy1lYXN02"
}
```