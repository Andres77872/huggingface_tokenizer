FROM python:3.12.3

WORKDIR /nn

COPY src /nn/src
COPY requirements.txt /nn

RUN pip3 install -r requirements.txt --break-system-packages
