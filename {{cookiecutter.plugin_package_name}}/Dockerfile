FROM python:3.7.4

RUN apt-get update && apt-get install -y cmake bison flex

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/

COPY setup.py /usr/src/app/
COPY README.md /usr/src/app/
COPY CHANGELOG.md /usr/src/app/

ARG target=.
RUN pip install -e "${target}"

COPY . /usr/src/app
