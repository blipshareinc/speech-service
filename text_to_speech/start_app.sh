#!/bin/sh

# download NLP Toolkit
python -m nltk.downloader averaged_perceptron_tagger

# this needs to change but it is required to do this as there is a badzip exception gets thrown
while true
do
    # start the app
    gunicorn --workers ${WORKERS} --bind ${HOST}:${PORT} 'app:app'
done