from flask import Blueprint

module = Blueprint('bundle_test', __name__)

@module.route('/', methods=['GET', 'POST'])
def test():
    return "Is a test"
