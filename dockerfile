FROM ubuntu:16.04

MAINTAINER "admin@whoorah.com"

RUN apt-get update -y && \
    apt-get install -y python3 && \
    apt-get upgrade -y python3 && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /flaskr/requirements.txt

WORKDIR /flaskr
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
RUN export LC_ALL=en_US.utf-8
RUN export LANG=en_US.utf-8
COPY . /flaskr

WORKDIR ../
ENTRYPOINT ["flask"]
CMD [ "run" ]
