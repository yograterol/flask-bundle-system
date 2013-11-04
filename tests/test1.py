import unittest
import os
from flask import url_for, Flask
from flaskext.bundle_system import BundleSystem


class SystemBundleTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        path = os.path.realpath(__file__)
        BundleSystem(self.app, os.path.dirname(path))
        self.app.config['TESTING'] = True
        ctx = self.app.test_request_context()
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

    def test_bundle_not_found(self):
        rv = self.web.get('/not-found')
        assert not 'Is a test' in rv.data

    def test_bundle_not_found_post(self):
        rv = self.web.post('/not-found')
        assert not 'Is a test' in rv.data

if __name__ == '__main__':
    unittest.main()
