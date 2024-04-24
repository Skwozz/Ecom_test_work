FROM python:3.11-alpine

WORKDIR /app

COPY ./Ecom .
COPY requirements.txt .
COPY ./run.sh .
ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt


CMD ["sh","run.sh"]
