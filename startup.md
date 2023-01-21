# How to Start the Program

1. activate the virtual environment
2. set the flask app by

    (a) cd'ing into ./canadaAps
   
    (b) export FLASK_APP=rentCanada.py
3. run "flask run"
4. new terminal. now run Celery.
   
    (a) again activate the venv
    
   (b) from project root, run 

5. "celery -A rentCanada canadaAps.canadaAps --loglevel=INFO" 