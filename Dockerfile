# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY app.py /app
COPY templates /app/templates

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]