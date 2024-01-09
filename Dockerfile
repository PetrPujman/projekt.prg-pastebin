FROM python:3.11

RUN apt-get update \
    && apt-get install --no-install-recommends -y default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

ENV WORKDIR=/code
WORKDIR $WORKDIR

ADD . /code/
RUN pip install --no-cache-dir -r requirements.txt
