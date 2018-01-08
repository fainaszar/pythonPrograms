FROM mikemanger/python27-mysql
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN pip install -r requirements.txt 

ADD . /code/
EXPOSE 8000


CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","createsuperuser"]
CMD ["python","manage.py","runserver","0.0.0.0:8000"]




