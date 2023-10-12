FROM python:3.9 AS base

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN chmod a+x docker/app.sh
