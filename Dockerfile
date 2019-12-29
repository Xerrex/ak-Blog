FROM python:3.6-alpine

RUN adduser -D blog

RUN mkdir -p /home/blog/akblog
WORKDIR /home/blog/akblog


COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN apk add --no-cache --virtual .build-deps python3-dev gcc build-base \
 && venv/bin/pip install --no-cache-dir -r requirements.txt \
 && apk del .build-deps
#RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY run.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

RUN chown -R blog:blog ./
USER blog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
