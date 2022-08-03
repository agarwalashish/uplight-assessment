import unittest
import requests
from unittest import TestCase
import json

class GenerateTokenApiTest(TestCase):
    url = 'http://localhost:5000/v1/generate-token'

    tokenRequestOne = {
        "message": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey."
    }

    tokenRequestTwo = {
        "id": "MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"
    }

    validHeader = {
        "Content-Type": "application/json",
        "client": "2ujhg51rasqsacvf0dwk",
        "secret": "usr2w4gqv6gwi4u8gc510zmr7h45q8yedcv8lv39"
    }

    invalidContentTypeHeader = {
        "Content-Type": "application/octet-stream",
        "client": "2ujhg51rasqsacvf0dwk",
        "secret": "usr2w4gqv6gwi4u8gc510zmr7h45q8yedcv8lv39"
    }

    invalidAuthHeader = {
        "Content-Type": "application/json",
        "client": "invalid_key",
        "secret": "invalid_secret"
    }

    def testCreateTokenOne(self):
        response = requests.post(self.url, data=json.dumps(self.tokenRequestOne), headers=self.validHeader)
        self.assertEqual(response.status_code, 200)

        responseData = eval(response.text)
        self.assertEqual(responseData["signature"], "69601504ee750274dd9571842b3141473ae099eb03e77e09154c1f12fc9eb8d2e612441856966eda41fc2bb26d92a5f38ba9d8b954cf2f1a14f3142b86eee98a")

    def testCreateTokenTwo(self):
        response = requests.post(self.url, data=json.dumps(self.tokenRequestTwo), headers=self.validHeader)
        self.assertEqual(response.status_code, 200)

        responseData = eval(response.text)
        self.assertEqual(responseData["signature"], "105d22b9853a92a0b5c2331ac6bb6c469dc7d0470bb9f9a851ae3efbc315821c18da7d2564d1680b664ff5ff1835fef20380cda45b8e7cd6febc970b297e996a")
    
    def testCreateTokenEmptyMessage(self):
        response = requests.post(self.url, headers=self.validHeader)
        self.assertEqual(response.status_code, 400)

    def testInvalidHeader(self):
        response = requests.post(self.url, data=json.dumps(self.tokenRequestOne), headers=self.invalidContentTypeHeader)
        self.assertEqual(response.status_code, 400)

    def testInvalidAuth(self):
        response = requests.post(self.url, data=json.dumps(self.tokenRequestOne), headers=self.invalidAuthHeader)
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()