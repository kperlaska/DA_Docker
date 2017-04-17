FROM debian:latest
MAINTAINER kristjan.perlaska <kristjan.perlaska@swisscom.com>

ENV http_proxy http://proxy.corproot.net:8079
ENV https_proxy http://proxy.corproot.net:8079



RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential \
                       libncursesw5-dev \
                       libreadline-dev \
                       libssl-dev \
                       libgdbm-dev \
                       libc6-dev \
                       libsqlite3-dev \
                       libxml2-dev \
                       libxslt-dev \
                       python \
                       python-dev \
                       python-setuptools \
                       python-pip 


RUN pip install locustio pyzmq

RUN apt-get clean

RUN mkdir /locust

WORKDIR /locust

ADD locustfile.py /locust

EXPOSE 8089 5557 5558

ENTRYPOINT ["/usr/local/bin/locust"]
