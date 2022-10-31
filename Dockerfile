# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# install dependencies
RUN apt-get update
RUN apt-get install -y python3-pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/