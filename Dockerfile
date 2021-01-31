FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN mkdir /bboard
WORKDIR /bboard

COPY Pipfile Pipfile.lock /bboard/

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN pip install pipenv && pipenv install --system

COPY . /bboard/
