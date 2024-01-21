FROM alpine:3.16    

ENV TZ=Europe/Prague

RUN apk add python3 py3-pip tzdata

RUN cp /usr/share/zoneinfo/Europe/Prague /etc/localtime

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD ./api /home/api

WORKDIR /home

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "api.main:api", "--host", "0.0.0.0"]