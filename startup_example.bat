@echo on
:: using anaconda env
call ..\Anaconda\Scripts\activate.bat
call activate FlaskEnv
set FLASK_APP=app.py
set FLASK_DEBUG=0
:: for this to work - it needs to be loacated in the same folder with your app.py
flask run