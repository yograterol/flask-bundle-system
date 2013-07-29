import unittest
from os import getcwd
from flask import url_for
from flaskext.bundle_system import BundleSystem


class SystemBundleTest(unittest.TestCase):

    def setUp(self):
        self.web = BundleSystem('test', True, None, getcwd(), True)
        self.web.load_module(['test1.py'])
        self.app = self.web.load_app()

    def test_url_for(self):
        url_test = url_for('bundle_test1.test')
        assert '/test/' in url_test

    def test_bundle(self):
        rv = self.app.get(url_for('bundle_test.test'))
        assert 'Is a test' in rv.data

    def test_bundle_post(self):
        rv = self.app.post(url_for('bundle_test.test'))
        assert 'Is a test' in rv.data

    def test_bundle_with_url_prefix(self):
        rv = self.app.get(url_for('bundle_test1.test'))
        assert 'Is a test' in rv.data

    def test_bundle_with_url_prefix_post(self):
        rv = self.app.post(url_for('bundle_test1.test'))
        assert 'Is a test' in rv.data

    def test_bundle_not_found(self):
        rv = self.app.get('/not-found')
        assert not 'Is a test' in rv.data

    def test_bundle_not_found_post(self):
        rv = self.app.post('/not-found')
        assert not 'Is a test' in rv.data

if __name__ == '__main__':
    unittest.main()
