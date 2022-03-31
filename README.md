# defect-prediction
This project relies on software metrics to predict defects in code
# Project Composition
The front end and the back end need to run seperately, so please open two terminal windows. 
## predef_prototype:
This has a preliminary version of the project on which we tested the feasability of the project.
## predef_v2
```
Go to predef_v2 by typing
```
cd predef_v2
This contains the project and all the necessary modules. In order to run the back end please type the following commands:
```
pip3 install flask 
pip3 install radon
pip3 install numpy
pip3 install scikit-learn
pip3 install pandas
```

Then please change the python path (place your path here):
```
export PYTHONPATH="/Users/waelbenamara/Desktop/defect-prediction/"
```
If we do not perform this step the interpreter will not be able to access multiple files.

Finally run the server file by typing:

```
python3 server.py
```
## front end
Go to the directory by typing 
```
cd front-defect-pred
```
To run it just type:
```
python3 server.py
```

# Rest API
In order to get a broad overview about the output returned by the project please use postman to send a GET requests to the following url
```
http://0.0.0.0:3030/analyse
```
with the following payload as request body (example)
```json
{
    "git_repo":"https://github.com/rubik/radon"
}
```
You should expect something like this in return:
```json
{
    "files": [
        "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/tests/test_simple.py",
        "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/tests/__init__.py",
        "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/setup.py",
        "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/src/sample/__init__.py",
        "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/src/sample/simple.py"
    ],
    "git_url": "https://github.com/pypa/sampleproject",
    "global_result": {
        "HalsteadProgramLength": 9,
        "LinesOfCode": 19,
        "LinesOfComments": 144,
        "McCabeCyclomaticComplexity": 0.7,
        "NumberOfOperands": 6,
        "NumberOfOperators": 3,
        "TotalNumberOfOperands": 6,
        "TotalNumberOfOperators": 3,
        "effort": 7.132331253245203,
        "prediction": 0,
        "volume": 14.264662506490406
    },
    "id": "23bcabc4-589b-11ec-9431-d4619d092a02",
    "path": "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02",
    "per_module_results": [
        {
            "HalsteadProgramLength": 3,
            "LinesOfCode": 7,
            "LinesOfComments": 3,
            "McCabeCyclomaticComplexity": 1.5,
            "NumberOfOperands": 2,
            "NumberOfOperators": 1,
            "TotalNumberOfOperands": 2,
            "TotalNumberOfOperators": 1,
            "effort": 2.3774437510817346,
            "filename": "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/tests/test_simple.py",
            "volume": 4.754887502163469
        },
        {
            "HalsteadProgramLength": 0,
            "LinesOfCode": 0,
            "LinesOfComments": 3,
            "McCabeCyclomaticComplexity": 0,
            "NumberOfOperands": 0,
            "NumberOfOperators": 0,
            "TotalNumberOfOperands": 0,
            "TotalNumberOfOperators": 0,
            "effort": 0,
            "filename": "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/tests/__init__.py",
            "volume": 0
        },
        {
            "HalsteadProgramLength": 3,
            "LinesOfCode": 7,
            "LinesOfComments": 138,
            "McCabeCyclomaticComplexity": 0,
            "NumberOfOperands": 2,
            "NumberOfOperators": 1,
            "TotalNumberOfOperands": 2,
            "TotalNumberOfOperators": 1,
            "effort": 2.3774437510817346,
            "filename": "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/setup.py",
            "volume": 4.754887502163469
        },
        {
            "HalsteadProgramLength": 0,
            "LinesOfCode": 3,
            "LinesOfComments": 0,
            "McCabeCyclomaticComplexity": 1.0,
            "NumberOfOperands": 0,
            "NumberOfOperators": 0,
            "TotalNumberOfOperands": 0,
            "TotalNumberOfOperators": 0,
            "effort": 0,
            "filename": "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/src/sample/__init__.py",
            "volume": 0
        },
        {
            "HalsteadProgramLength": 3,
            "LinesOfCode": 2,
            "LinesOfComments": 0,
            "McCabeCyclomaticComplexity": 1.0,
            "NumberOfOperands": 2,
            "NumberOfOperators": 1,
            "TotalNumberOfOperands": 2,
            "TotalNumberOfOperators": 1,
            "effort": 2.3774437510817346,
            "filename": "predef_v2/projects/23bcabc4-589b-11ec-9431-d4619d092a02/src/sample/simple.py",
            "volume": 4.754887502163469
        }
    ]
}
```
