FROM python:3.6-alpine

COPY . /loulin

RUN cd /loulin \
    && python -m venv venv \
    && venv/bin/pip install -r requirements.txt \
    && venv/bin/pip install gunicorn \
    && export FLASK_APP=manage.py


EXPOSE 5000



