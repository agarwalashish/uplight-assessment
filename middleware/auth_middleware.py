
from os import stat
from werkzeug.wrappers import Request, Response, ResponseStream

class AuthMiddleware:

    # Hardcode client id and secret for now. The request will check to see if the provided client id and secret match these values
    clientId = "2ujhg51rasqsacvf0dwk"
    clientSecret = "usr2w4gqv6gwi4u8gc510zmr7h45q8yedcv8lv39"

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        if 'Client' in request.headers and 'Secret' in request.headers:
            clientId = request.headers['Client']
            clientSecret = request.headers['Secret']

            if clientId == self.clientId and clientSecret == self.clientSecret:
                return self.app(environ, start_response)

        response = Response('{"error": "Authentication failed"}', mimetype='application/json', status=401)
        return response(environ, start_response)