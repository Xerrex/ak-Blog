FROM python:3.7-alpine

RUN adduser -D blog

RUN mkdir -p /home/blog/akblog
WORKDIR /home/blog/akblog


COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN apk add --no-cache gcc musl-dev linux-headers python3-dev libffi-dev libressl-dev
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql
RUN venv/bin/pip install cryptography

COPY app app
COPY migrations migrations
COPY run.py config.py boot.sh ./
RUN chmod +x "boot.sh"

ENV FLASK_APP run.py

RUN chown -R blog:blog ./
USER blog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
