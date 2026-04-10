from app import app
import unittest
from unittest.mock import patch


class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @patch('app.get_db')
    def test_health(self, mock_db):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})


if __name__ == '__main__':
    unittest.main()
