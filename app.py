from flask import Response, request, jsonify
import flask
import io
import json
import yaml
from src.exceptions import ApiException, BadRequestException
from src.services.signature_generator import SignatureGenerator
import os


app = flask.Flask(__name__)
app.config['DEBUG'] = True

with open('configurations.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

signatureGenerator = SignatureGenerator(config)

vals = os.path.split(os.path.abspath('app.py'))


@app.route('/v1/generate-token', methods=['POST'])
def generateSignature():
    if request.headers.get('Content-Type') != 'application/json':
        raise BadRequestException()
    
    content = request.get_json()

    # Generate the signature of the request body
    signature = signatureGenerator.generate(json.dumps(content))

    # Add the signature to the body of the request received
    content['signature'] = signature

    return Response(json.dumps(content), status=200)

# Handler for all the different API exceptions
@app.errorhandler(ApiException)
def handleException(err):
    """Return a json when an exception is thrown"""
    response = {"error": err.error, "code": err.code}
    if len(err.args) > 0:
        response["error"] = err.args[0]
    return jsonify(response), err.code


app.run()