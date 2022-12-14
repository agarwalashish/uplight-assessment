from flask import Response, request, jsonify
import flask
import json
import yaml
from exceptions import ApiException, BadRequestException
from services.signature_generator import SignatureGenerator
from middleware.auth_middleware import AuthMiddleware

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.wsgi_app = AuthMiddleware(app.wsgi_app)

with open('configurations.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

signatureGenerator = SignatureGenerator(config)

@app.route('/v1/generate-token', methods=['POST'])
def generateSignature():
    if request.headers.get('Content-Type') != 'application/json':
        raise BadRequestException()

    # Check if the post request has a body
    if not request.data:
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