# Get a Token from user and password
[Back](../README.MD)

If Callevo's administration provides you with a username and password to operate in the system, you will need to obtain the token with the following steps.

1. Authenticate as a user, to do this you must execute the path POST/authuser and it must be defined in the file `.env` ([how to create the file](/doc/create_environment_file.md)).
### AuthLogin
2. Open a file [`src/users/post-authlogin.py`](/src/users/post-authlogin.py)  and check if usertype is the correct with the one given by Callevo Administration.<br>
```
    2 - Administrator <br>
    27 - Agent <br> 
    30 - Agent <br> 
```
3. Run the file `python src/users/post-authlogin.py`
4. Select an collect the userid
### Auth User
5. Open file  [`src/users/post-authuser.py`](/src/users/post-authuser.py)  and change the userid with the userid value.
6. Run the file `python src/users/post-authuser.py`
7. Get a token parameter and put into environment file

