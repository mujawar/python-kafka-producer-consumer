FROM python:3.7.0
RUN apt-get update -yqq && \
apt-get -y install curl

RUN apt-get update
RUN pip install --upgrade pip
WORKDIR /src
COPY data_genarater.py /src/
COPY kafka_producer.py /src/
COPY kafka_consumer.py /src/
COPY requirement.txt /src/


RUN pip install -r requirement.txt

ENTRYPOINT [ "python","kafka_producer.py"] 
