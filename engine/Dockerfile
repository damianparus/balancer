FROM python:3.10.1-alpine3.15

RUN mkdir /opt/balancer
WORKDIR /opt/balancer

COPY ./requirements.txt requirements.txt
COPY ./src/*.py src/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "src/main.py", "--fronius-url", "http://192.168.1.10/"]
