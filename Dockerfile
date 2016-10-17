FROM python:3
 
WORKDIR /opt/app

ADD . /opt/app

RUN pip3 install -r requirements.txt

EXPOSE 8888

CMD /bin/sh app.sh
