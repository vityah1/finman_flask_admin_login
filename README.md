Financial manager 0.0.1 with flask_admin and flask_login

Small and compact back-end rest-api written on flask with flask_admin and flask_login.  

Instalation:
## Requirements
This simple solution and practise for use flask, app factory tohnologi

## Instalation:

1. pip3 install -r requirements.txt

## Configuration and setting
2. create and edit simple txt finman_config.json file with next structure:

```json
{
"db_host": "your_db_host",
"db_user": "db_user",
"db_passwd": "db_password",
"db_db": "db_name",
"secret_key": "your_super_secret_key",
"dict_phones":{"+80380501112233":"name1","0631112233":"name2"},
"not_sub_cat":["AliExpress"],
"not_cat":["Грошові перекази"],
    "DEVELOPMENT_DATABASE_URI": "mysql+pymysql://...",
    "PRODUCTION_DATABASE_URI": "mysql+pymysql://...",
    "TESTING_DATABASE_URI": "mysql+pymysql://...",
    "SECRET_KEY": "your_super_secret_key",
    "MAIL_USERNAME": "e-mail",
    "MAIL_PASSWORD": "mail password",
    "MAIL_SERVER": "mail server",
}
```

## Create database tables
3. As I use SQLMigrate You can set conn pars in json file.
set FLASK_APP to manage.py and execute 
flask db init
flask db upgrade

## Local run
4. flask run if you run it localy

## Virtual apache shared hosting
#5. edit .htaccess file according to your paths
# not realized yet



