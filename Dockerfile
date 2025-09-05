FROM python:3.11-alpine

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install "fastapi[standard]"

CMD ["fastapi", "run", "main.py"]