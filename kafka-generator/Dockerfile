FROM python:3-alpine

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN apk add --no-cache librdkafka && apk add --no-cache librdkafka-dev
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ADD GenerationСheque ./GenerationСheque
WORKDIR /usr/app/src/GenerationСheque

CMD [ "python", "main.py" ]