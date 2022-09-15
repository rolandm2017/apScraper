# syntax=docker/dockerfile:1
FROM 3.10.5-bullseye
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask
RUN pip install requests
EXPOSE 5000
COPY . .
CMD ["flask", "run"]