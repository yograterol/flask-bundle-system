from flask import Blueprint

module = Blueprint('bundle_test', __name__)

@module.route('/')
def test():
    return "Is a test"
