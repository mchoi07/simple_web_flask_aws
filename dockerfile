FROM ubuntu:16.04

MAINTAINER "admin@whoorah.com"

RUN apt-get update -y && \
    apt-get install -y python3.6 python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /flaskr/requirements.txt

WORKDIR /flaskr
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export FLASK_APP=flaskr
RUN export FLASK_ENV=development
RUN export LC_ALL=en_US.utf-8
RUN export LANG=en_US.utf-8
COPY . /flaskr

WORKDIR ../
ENTRYPOINT ["flask"]
CMD [ "run" ]
