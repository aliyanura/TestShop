FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /TestShop

COPY requirements.txt /TestShop/
RUN pip install -r requirements.txt

COPY . /TestShop/

RUN mkdir -p /back_media
RUN mkdir -p /back_static

