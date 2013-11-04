====================
flask-bundle-system
====================

Install
=======

```
pip install http://github.com/yograterol/flask-bundle_system/zipball/master
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
from flaskext.bundle_system import BundleSystem

# Define the Flask App
app = Flask(__name__)
# Get the current main dir path for the app.
path = ...
# Register all blueprint as bundles.
BundleSystem(app, path)
```

Test
====

```
python setup.py nosetests
```

Travis CI
=========

[![Build Status](https://travis-ci.org/yograterol/flask-bundle-system.png?branch=master)](https://travis-ci.org/yograterol/flask-bundle-system)
