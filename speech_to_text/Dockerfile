FROM python:3.6.15-slim

COPY . /app

WORKDIR /app

RUN apt-get update && \
    apt-get install -y sox &&\
    python3 -m venv env && \
    . env/bin/activate && \
    pip3 install -r requirements.txt

ENV PYTHONPATH=/app:$PYTHONPATH
ENV PATH=./env/bin:$PATH

EXPOSE $PORT

CMD ["/bin/sh", "-c", "gunicorn --workers ${WORKERS} --bind ${HOST}:${PORT} 'app:app'"]