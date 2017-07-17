FROM debian:latest
MAINTAINER kristjan.perlaska <kristjan.perlaska@swisscom.com>

ENV type "" 

ENV masterip ""

ENV user ""

ENV hatchrate ""

ENV host https://www-uat.juliusbaer.com

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
                       python-pip \
                       curl 


RUN pip install locustio pyzmq beautifulsoup4

RUN apt-get clean

RUN mkdir /locust

WORKDIR /locust

ADD locustfile.py /locust

EXPOSE 8089 5557 5558 80 

ENTRYPOINT /usr/local/bin/locust --host=$host $type $masterip $user $hatchrate -P 80 &> /dev/null
