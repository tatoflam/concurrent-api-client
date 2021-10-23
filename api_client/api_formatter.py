from api_client.constants import URLS, PATHS

class ApiFormatter:
    """ a template formatter base for building  API request
    """    
    def __init__(self, environment=None, token=None):
        self.host_url = URLS[environment]
        self.paths = PATHS
        self.token = token

    def get_url(self):
        pass

    # Default header with "Authorization: Bearer" is generated here in super class.
    # If an API does not expect this header format, Formatter subclass can override get_header()
    def get_headers(self):
        if self.token :
            headers = {
                "Authorization": "Bearer {}".format(self.token),
                "content-type": "application/json"
            }
            return headers
        else:
            pass

    def get_params(self):
        pass
