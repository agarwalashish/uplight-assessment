import hmac
import hashlib


class SignatureGenerator:

    def __init__(self, config):
        self.config = config

    def generate(self, message):
        secret = self.config['hmac_key']
        encodedMessage = hmac.new(key=bytes(secret, 'UTF-8'), msg=bytes(message, 'UTF-8'), digestmod=hashlib.sha512)
        signature = encodedMessage.hexdigest()
        return signature


