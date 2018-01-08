FROM mysql

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD diamonds.csv /code/
EXPOSE 8000
EXPOSE 3600
ADD . /code/


RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install python-pip

RUN apt-get -y install python-dev
RUN apt-get -y install redis-server

RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools
RUN python -m pip install pymysql
RUN python -m pip install redis