import unittest 

from api_client.api_formatter import ApiFormatter

class TestApiFormatter(unittest.TestCase):
    def test_get_headers(self):
        
        token = 'foo'
        api_formatter = ApiFormatter(token)
        
        returned = api_formatter.get_headers()
        
        expected = {
                "Authorization": "Bearer {}".format(token),
                "content-type": "application/json"
            }
        
        self.assertDictEqual(returned, expected)        
