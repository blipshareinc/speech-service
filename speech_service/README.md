**<span style="color:yellow">WORK-IN-PROGRESS</span>**
# Home Automation Voice Module
This is the voice addon for the home automation project. It consists of two microservices hosted in containers.

## 1. Speech-To-Text Service
This service takes a `.wav` audio file as input and returns the corresponding text for the audio file. It utilizes DeepSpeech model to do so.

### To-Dos:

* Create a `virtual` env and install the following packages
  <ul>
    <li>Gunicorn</li>
    <li>deepspeech</li>
    <li>tensorflow</li>
  </ul>

* Create a python web app to listen for requests with `.wav` file as an input and provide the text as output to the client

* Create a `requirements.txt` file

* Create a `Dockerfile`

## 2. Text-To-Speech Service
This Service takes text as input and converts and returns a `.wav` audio file. It utilizes fastspeech2 model to do so.

### To-Dos:
* Create a `virtual` env and install the following packages
  <ul>
    <li>Gunicorn</li>
    <li>fastspeech2</li>
  </ul>

* Create a python web app to listen for request with `text` as an input and return a `.wav` as an output to the client

* Create a `requirements.txt` file

* Create a `Dockerfile`

## Productionize
The following steps should be done once both services can run as services in a container

### 1. Facilitate Containers
Create `dockercompose` file to facilitate both containers

### 2. Version Control
<ol>
  <li> Save the images on <em>docker hub</em> </li>
  <li> Save the app files on <em>github</em> </li>
</ol>

