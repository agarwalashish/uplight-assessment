import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from services.signature_generator import SignatureGenerator

class SignatureGeneratorTest(TestCase):

    # Setup the unit tests 
    def setUp(self):
        #Create a mock of the configuration that will be passed into the SignatureGenerator
        self.config = MagicMock()
        values = {'hmac_key': 'secret'}
        self.config.__getitem__.side_effect = values.__getitem__
        self.signatureGenerator = SignatureGenerator(self.config)

    def testGenerateSignature(self):        
        signature = self.signatureGenerator.generate("test message")
        self.assertTrue(signature == "4ca0748eaeaaf0789d1a4785c5c5ccb4421c97c558f763c8c09eaf96ce71b805e8f670c9368c869dc994554508d6729b4d022a72718e5a6a9ae1ba1f6dedf4b5")
    
    def testGenerateSignatureEmptyMessage(self):
        signature = self.signatureGenerator.generate("")
        self.assertEqual(signature, None)

if __name__ == '__main__':
    unittest.main()