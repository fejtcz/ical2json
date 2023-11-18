FROM alpine:3.16

RUN apk add python3 py3-pip

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . /home

WORKDIR /home
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "api.main:api", "--host", "0.0.0.0"]