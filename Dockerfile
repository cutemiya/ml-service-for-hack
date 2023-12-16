FROM python:3.8-slim-buster

WORKDIR /app

COPY ./ml-service-for-hack/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ml-service-for-hack .

CMD ["uvicorn", "main:app", "--port", "1488"]

EXPOSE 1488