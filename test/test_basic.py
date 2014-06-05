import os
import application
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        application.app.config['TESTING'] = True
        self.app = application.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        assert 'Hello World' in rv.data

if __name__ == '__main__':
    unittest.main()
