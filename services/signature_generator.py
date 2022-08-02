import hmac
import hashlib

from numpy import sign

class SignatureGenerator:
    def __init__(self, key):
        self.secret_key = key

    def generate(self, message, secret):
        encodedMessage = hmac.new(key=bytes(secret, 'UTF-8'), msg=bytes(message, 'UTF-8'), digestmod=hashlib.sha512)
        signature = encodedMessage.hexdigest()
        return signature


