FROM tensorflow/tensorflow:2.7.0-gpu

RUN rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update && apt-get install -y git cmake libsndfile1

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt && \
    pip install git+https://github.com/TensorSpeech/TensorflowTTS.git

ENV PYTHONPATH=/app:$PYTHONPATH

EXPOSE $PORT

CMD ["/bin/sh", "-c", "./start_app.sh"]
