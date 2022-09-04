**<span style="color:yellow">WORK-IN-PROGRESS</span>**
# Speech Service
This is the voice addon for the home automation project. It consists of two microservices hosted in containers.

## 1. Speech-To-Text Service
This service takes a `.wav` audio file as input and returns the corresponding text for the audio file. It utilizes DeepSpeech model to do so. [Read more](./speech_to_text/README.md)

## 2. Text-To-Speech Service
This Service takes text as input and converts and returns a `.wav` audio file. It utilizes fastspeech2 model to do so. [Read more](./text_to_speech/README.md)