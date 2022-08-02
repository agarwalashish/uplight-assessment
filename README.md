# HMAC Token Generation

A POST endpoint that generates a HMAC token for the request payload


## Description

The API endpoint is:

```
/v1/generate-token
```

The endpoint will accept a POST request with a JSON payload, generate a HMAC token and add it as a signature property to request's payload.

### Example 1:

**Request**
```
curl -X POST \
-H "Content-Type: application/json" \
'localhost:5000/v1/generate-token' \
--data '{"id": "MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"}'
```

**Response**
```
{
  "id": "MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz",
  "signature": "105d22b9853a92a0b5c2331ac6bb6c469dc7d0470bb9f9a851ae3efbc315821c18da7d2564d1680b664ff5ff1835fef20380cda45b8e7cd6febc970b297e996a"
}
```

### Example 2:
**Request**
```
curl -X POST \
-H "Content-Type: application/json" \
'localhost:5000/v1/generate-token' \
--data '{"message":"Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey."}'
```

**Response**
```
{
  "message": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey.",
  "signature": "69601504ee750274dd9571842b3141473ae099eb03e77e09154c1f12fc9eb8d2e612441856966eda41fc2bb26d92a5f38ba9d8b954cf2f1a14f3142b86eee98a"
}
```

## Folder Structure

```
├── README.md
├── app.py
├── configurations.yaml
├── requirements.txt
└── src
    ├── exceptions.py
    └── services
        └── signature_generator.py
```

**app.py**: is the entry point of the application.

**configurations.yaml**: Contains all the configurations for the application. Currently, only one environment is supported.

**requirements.txt**: All the dependencies used by the project.

**src**: The directory where the source code is contained. 

## Building locally

* Run `pip install -r requirements.txt` to install all the python dependencies
* Run `python app.py` to start the server locally

## Running tests 

`python -m unittest discover -s tests -p '*test.py'` will run all the tests