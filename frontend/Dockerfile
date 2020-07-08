FROM python:3.8-alpine

WORKDIR /app
COPY src/ /app/src/
COPY requirements /app
COPY application.ini /app
COPY main.py /app

RUN python3 -m pip install -r requirements

ENV ENVIRONMENT DEV
EXPOSE 8000
CMD ["python", "/app/main.py"]