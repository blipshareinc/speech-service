from flask import Flask, request, jsonify
from os import path, environ
import subprocess

def _process(input_file):
    if input_file and path.exists(input_file):
        cmd = ["deepspeech --model ./models/deepspeech-0.9.3-models.pbmm --audio %s" % input_file]

        # execute the command in the shell
        sub_p = subprocess.Popen(args=cmd, env=dict(environ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = sub_p.communicate()

        if stdout:
            print(stdout)
            return stdout.decode('ascii').strip()

        if stderr:
            print("ERROR: %s" % stderr)
            print(stderr)
            return "ERROR: Please try again"


app = Flask("DeepSpeech")

@app.route('/stt', methods=['POST'])
def stt():
    '''
    Description: Function to listen for user request with json parameters to convert speech to text.
    It takes in the following parameters:
    name: Requesting User's name.
    input_file: Path to the speech (.wav) file to be converted to text
    @return: jsonify string.
    '''

    requestor = 'Not Available'
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if json and 'name' in json:
            if 'input-file' in json:
                requestor = json['name']
                input_file = json['input-file']
                text = _process(input_file)
                return jsonify({'requestor': requestor, 'data': text})

    return jsonify({'requestor': requestor, 'data': 'unavailable'})

#app.run(host="0.0.0.0", port="11001", debug=True)