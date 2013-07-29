from flask import Blueprint

bundle_config = {'url_prefix': '/test'}
bundle = Blueprint('bundle_test1', __name__)

@bundle.route('/', methods=['GET', 'POST'])
def test():
    return "Is a test"
