FROM python:3.8-alpine

WORKDIR /app
COPY src/ /app/src/
COPY requirements /app
COPY main.py /app

RUN python3 -m pip install -r requirements

CMD ["python", "/app/main.py"]