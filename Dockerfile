FROM python:3.11.0rc1-alpine3.16
WORKDIR /code
ENV FLASK_APP=./canadaAps/rentCanada.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8001
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8082"]
CMD [ "celery", "-A", "canadaAps.rentCanada", "worker", "--loglevel=INFO"]