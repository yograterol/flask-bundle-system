import unittest
import os
from flask import url_for, Flask
from flask_bundlesystem import BundleSystem


class SystemBundleTest(unittest.TestCase):

    def setUp(self):
        # Set a Flask App
        app = Flask(__name__)
        path = os.path.realpath(__file__)
        app.config['TESTING'] = True

        with app.test_request_context() as ctx:
            # Call to extension for register blueprints
            BundleSystem(os.path.dirname(path))
            ctx.push()
            self.web = ctx.app.test_client()

    def test_url_for(self):
        url_test = url_for('bundle_test1.test')
        assert '/test/' in url_test

    def test_bundle(self):
        rv = self.web.get(url_for('bundle_test.test'))
        assert 'Is a test' in rv.data, rv.data

    def test_bundle_post(self):
        rv = self.web.post(url_for('bundle_test.test'))
        assert 'Is a test' in rv.data

    def test_bundle_with_url_prefix(self):
        rv = self.web.get(url_for('bundle_test1.test'))
        assert 'Is a test' in rv.data

    def test_bundle_with_url_prefix_post(self):
        rv = self.web.post(url_for('bundle_test1.test'))
        assert 'Is a test' in rv.data


if __name__ == '__main__':
    unittest.main()
