FROM tensorflow/tensorflow:2.7.0-gpu

RUN rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update && apt-get install -y git cmake libsndfile1

COPY ./fastspeech2.py /app/fastspeech2.py
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py

WORKDIR /app

RUN pip install -r requirements.txt && \
    pip install git+https://github.com/TensorSpeech/TensorflowTTS.git

ENV PATH=./env/bin:$PATH

EXPOSE 11000

CMD ["python3", "app.py"]
