FROM python:3.11.7-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "encurtador_url.wsgi:application", "-k", "gevent"]
