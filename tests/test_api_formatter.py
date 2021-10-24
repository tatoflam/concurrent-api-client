import unittest 

from api_client.api_formatter import ApiFormatter

class TestApiFormatter(unittest.TestCase):
    def test_get_headers(self):
        url = 'https://any-api'
        path = '/any-endpoint/'
        token = 'foo'
        api_formatter = ApiFormatter(url=url, path=path, token=token)
        
        returned = api_formatter.get_headers()
        
        expected = {
                "Authorization": "Bearer {}".format(token),
                "content-type": "application/json"
            }

        self.assertDictEqual(returned, expected)
        
    def test_no_headers(self):
        url = 'https://any-api'
        path = '/any-endpoint/'
        api_formatter = ApiFormatter(url=url, path=path, token=None)
        
        returned = api_formatter.get_headers()
        expected = None
        
        self.assertEqual(returned, expected)
