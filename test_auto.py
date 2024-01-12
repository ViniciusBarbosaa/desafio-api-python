import unittest
from flask import Flask
from app import app

class TestConvertCurrency(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_convert_currency_successful(self):
        response = self.app.get('/convert?from=USD&to=BRL&amount=100.00')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('from', data)
        self.assertIn('to', data)
        self.assertIn('amount', data)
        self.assertIn('result', data)

    def test_convert_currency_invalid_currency(self):
        response = self.app.get('/convert?from=XYZ&to=BRL&amount=100.00')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_convert_currency_invalid_amount(self):
        response = self.app.get('/convert?from=USD&to=BRL&amount=invalid_value')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
    