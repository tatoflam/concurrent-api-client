from api_client.api_client import ApiClient
from api_client.api_formatter import ApiFormatter

from logging import getLogger
import json

logger = getLogger(__name__)


URL = 'https://weather.tsukumijima.net'
PATH = '/api/forecast'

class WheatherApiFormatter(ApiFormatter):
    """LearningInstanceFormatter : a formatter for learning instance endpoint

    :param ApiFormatter: formatter base class
    :type ApiFormatter: Exception
    """    
    def __init__(self, url, path, token, city_code):
        self.url = url
        self.path = path
        self.token = token
        self.city_code = city_code

    def get_url(self):
        return  "{}{}".format(self.url, self.path)

    def get_params(self):
        params = {
            "city": self.city_code
        }
#        return json.dumps(params)
        return params

def test_weather_api():    
    apiclient = ApiClient( WheatherApiFormatter(url=URL, path=PATH, token=None, city_code=130010) )
    url, headers, params, res_json, status = apiclient.get()