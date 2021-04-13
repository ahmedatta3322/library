ECHO OFF
cd venv
cd Scripts
call activate
cd .. 
cd ..
SET FLASK_APP=main.py
SET FLASK_DEBUG=TRUE
flask run
PAUSE