from importlib.resources import contents
from flask import request, jsonify
import flask
import io
import json
import yaml

from services.signature_generator import SignatureGenerator


app = flask.Flask(__name__)
app.config['DEBUG'] = True

signatureGenerator = SignatureGenerator('abc')

with open('configurations.yaml', 'r') as stream:
    configs = yaml.safe_load(stream)


@app.route('/v1/generate-token', methods=['POST'])
def generateSignature():
    if request.headers.get('Content-Type' != 'application/json'):
        return "Invalid content type"
    
    content = request.get_json()
    hmacKey = configs['hmac_key']

    signature = signatureGenerator.generate(json.dumps(content), hmacKey)
    content['signature'] = signature
    return content


app.run()