import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        tester = app.test_client(self)
        response = tester.get('/1')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        tester = app.test_client(self)
        response = tester.get('/create')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
