from flask import Flask, request, jsonify
import json
from fastspeech2 import process

app = Flask("FastSpeech2")

@app.route('/tts', methods=['POST'])
def tts():
    '''
    Description: Function to listen for user request with json parameters to convert text to speech.
    It takes in the following parameters:
    name: Requesting User's name.
    text: Text to be converted to audio.
    @return: jsonify string.
    '''

    requestor = 'Not Available'
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if json and 'name' in json:
            if 'text' in json:
                requestor = json['name']
                text = json['text']
                if len(json) > 0:
                    audio_file_path = process(text, '/app/output')
                    return jsonify({'requestor': requestor, 'data': audio_file_path})

    return jsonify({'requestor': requestor, 'data': 'unavailable'})
