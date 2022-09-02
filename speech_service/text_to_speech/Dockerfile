FROM tensorflow/tensorflow:2.7.0-gpu

RUN rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update && apt-get install -y git cmake libsndfile1 && \
    pip install pydantic==1.9.1 && \
    pip install git+https://github.com/TensorSpeech/TensorflowTTS.git

COPY ./fastspeech2.py /app/fastspeech2.py

WORKDIR /app

EXPOSE 11000

CMD ["python3", "fastspeech2.py"]
