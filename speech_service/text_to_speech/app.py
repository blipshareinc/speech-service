from flask import Flask, request, jsonify
import json
from fastspeech2 import process

app = Flask("FastSpeech2")

@app.route('/tts', methods=['POST'])
def tts():
    requestor = 'Not Available'
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if json and 'name' in json:
            if 'text' in json:
                requestor = json['name']
                text = json['name']
                if len(json) > 0:
                    audio_file_path = process(text, '/app/output')
                    return jsonify({'requestor': requestor, 'data': audio_file_path})

    return jsonify({'requestor': requestor, 'data': 'unavailable'})

app.run(host='0.0.0.0', port=11000, debug=True)
