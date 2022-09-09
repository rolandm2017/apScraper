FROM python:3.11.0rc1-alpine3.16
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask
RUN pip install requests
EXPOSE 8083
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8083"]