FROM python:3.11

ENV WORKDIR=/code
WORKDIR $WORKDIR

ADD . /code/
RUN pip install --no-cache-dir -r requirements.txt
