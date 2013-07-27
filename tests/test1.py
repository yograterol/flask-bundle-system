import unittest
from os import getcwd
from flaskext.system_bundle import SystemBundle


class SystemBundleTest(unittest.TestCase):

    def setUp(self):
        self.web = SystemBundle('test', True, None, getcwd(), True)
        self.web.load_module(['test1.py'])
        self.app = self.web.load_app()

    def test_bundle_test(self):
        rv = self.app.get('/')
        assert 'Is a test' in rv.data

if __name__ == '__main__':
    unittest.main()
