FROM python:latest
MAINTAINER Julio Nunez "jcn327@nyu.edu"

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y python3 
RUN apt-get install -y sqlite3
RUN apt-get install -y git
RUN git clone https://github.com/jcn20/AppSec_Flask_V.git
RUN pip3 install python-dotenv
WORKDIR /AppSec_Flask_V

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 8080
CMD python3 -m flask run --host=0.0.0.0 --port=8080
