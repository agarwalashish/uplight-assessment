import unittest
from unittest import mock, TestCase
from unittest.mock import mock_open, MagicMock
import yaml
from services.signature_generator import SignatureGenerator

class SignatureGeneratorTest(TestCase):

    def testGenerate(self):
        config = self.createMockConfig()
        signatureGenerator = SignatureGenerator(config)
        v = signatureGenerator.generate("test message")
        print(v)
        self.assertTrue(v == "4ca0748eaeaaf0789d1a4785c5c5ccb4421c97c558f763c8c09eaf96ce71b805e8f670c9368c869dc994554508d6729b4d022a72718e5a6a9ae1ba1f6dedf4b5")
    
    def createMockConfig(self):
        config = MagicMock()
        values = {'hmac_key': 'secret'}
        config.__getitem__.side_effect = values.__getitem__
        return config

if __name__ == '__main__':
    unittest.main()