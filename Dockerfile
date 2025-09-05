FROM python:3.11-alpine

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install "fastapi[standard]"

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]