# Flask Logging Demo

Supporting code for the Flask Logging demo:

`git clone <giturl>.git && cd logging_demo && python3 -m venv venv`

## Single Application File Example:
```
1. source venv/bin/activate
2. cd single_file_app_pattern
3. pip install -r requirements.txt
4. flask run
5. curl http://localhost:5000/
```

## Application Factory Pattern Example:
This pattern supports configuration via .env file as well as ENV_VAR
```
1. source venv/bin/activate
2. cd app_factory_pattern
3. pip install -r requirements.txt
4. flask run
5. curl http://localhost:5000
```
