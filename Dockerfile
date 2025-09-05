FROM python:3.11-alpine

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ['fastapi', 'run', 'main.py']