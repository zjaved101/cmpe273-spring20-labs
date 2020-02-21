# Lab 2

## Pre-requisites

* Install _Pipenv_

```
pip install pipenv
```

* Install _[Flask](https://palletsprojects.com/p/flask/)_

```
pipenv install flask==1.1.1
```

Once you have installed, you will see _Pipfile_ and _Pipfile.lock_ files under working directory.

* Install _pytest_ for development, not for production.

```
pipenv install pytest --dev
```

* Run this command to see the dependency graph

```
pipenv graph
```

* Create a file called _app.py_ and add this code snippet.

```python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

* Run your Hello World Flask application from a shell/terminal.

```sh
pipenv shell
$ env FLASK_APP=app.py flask run
```

* Open [this URL](http://127.0.0.1:5000/) in a web browser or run this CLI to see the output.

```
curl -i http://127.0.0.1:5000/
```

## Requirements

You will be building a RESTful class registration API in this lab.

### Domain Model

```
|-------|               |---------|
| Class |* ---------- * | Student |
|-------|               |---------|
```

### REST Endpoints to be implemented.

* Create a new student

```
POST /students

# Request
{
    "name": "Bob Smith"
}

# Response
# HTTP Code: 201
{
    "id" : 1234456,
    "name" : "Bob Smith"
}
```

* Retrieve an existing student

```
GET /students/{id}

{
    "id" : 1234456,
    "name" : "Bob Smith"
}
```

* Create a class

```
POST /classes

# Request
{
    "name": "CMPE-273"
}

# Response
{
    "id": 1122334,
    "name": "CMPE-273",
    "students": []
}
```

* Retrieve a class

```
GET /classes/{id}

{
    "id": 1122334,
    "name": "CMPE-273",
    "students": []
}
```

* Add students to a class

```
PATCH /classes/{id}

# Request
{
    "student_id": 1234456
}

# Response
{
    "id": 1122334,
    "name": "CMPE-273",
    "students": [
        {
            "id" : 1234456,
            "name" : "Bob Smith"
        }
    ]
}

```



