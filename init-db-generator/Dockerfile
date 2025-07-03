FROM python:3-alpine

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ADD Generator ./Generator
WORKDIR /usr/app/src/Generator

CMD [ "python", "main.py"]