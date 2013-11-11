====================
flask-bundle-system
====================

Work on Python 2.6 and Python 2.7.

Install
=======

```
pip install http://github.com/yograterol/flask-bundle-system/zipball/master

or

pip install flask-bundle-system
```

Use
===
In the blueprint files or modules files:

```
from flask import Blueprint

# Define blueprint with name "bundle"
bundle = Blueprint(...)
```

In the main file:

```python
from flask_bundlesystem import BundleSystem

# Define the Flask App
app = Flask(__name__)
# Get the current main dir path for the app.
path = ...

with app.app_context():
    # Register all blueprint as bundles.
    BundleSystem(path)
```

Test
====

```
python setup.py nosetests
```

Travis CI
=========

[![Build Status](https://travis-ci.org/yograterol/flask-bundle-system.png?branch=master)](https://travis-ci.org/yograterol/flask-bundle-system)
