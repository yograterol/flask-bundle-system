import unittest
from os import getcwd
from flaskext.system_bundle import SystemBundle


class SystemBundleTest(unittest.TestCase):

    def setUp(self):
        self.web = SystemBundle('test', True, None, getcwd(), True)
        self.web.load_module(['test1.py'])
        self.app = self.web.load_app()

    def test_bundle(self):
        rv = self.app.get('/')
        assert 'Is a test' in rv.data

    def test_bundle_post(self):
        rv = self.app.post('/')
        assert 'Is a test' in rv.data

    def test_bundle_not_found(self):
        rv = self.app.get('/not-found')
        assert not 'Is a test' in rv.data

    def test_bundle_not_found_post(self):
        rv = self.app.post('/not-found')
        assert not 'Is a test' in rv.data

if __name__ == '__main__':
    unittest.main()
