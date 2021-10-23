from logging import getLogger
import json

from api_client.api_formatter import ApiFormatter

logger = getLogger(__name__)

class WheatherApiFormatter(ApiFormatter):
    """LearningInstanceFormatter : a formatter for learning instance endpoint

    :param ApiFormatter: formatter base class
    :type ApiFormatter: Exception
    """    
    def __init__(self, environment, city_code):
        ApiFormatter.__init__(self, environment)
        self.path = self.paths['FORECAST']
        self.city_code = city_code

    def get_url(self):
        return  "{}{}".format(self.host_url, self.path)

    def get_params(self):
        params = {
            "city": self.city_code
        }
#        return json.dumps(params)
        return params