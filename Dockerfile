# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install pyodbc (and, optionally, sqlalchemy)
RUN pip3 install --trusted-host pypi.python.org pyodbc==4.0.26

COPY . .
#EXPOSE 8000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
