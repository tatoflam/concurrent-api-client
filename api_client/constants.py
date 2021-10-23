import os

BASE_DIR = os.path.dirname(__file__)
PORT = 443
API_CONNECTION_POOL_SIZE = 5
API_CLIENT_THREAD_POOL_SIZE = 5
LOGGING_CONF = os.path.join(BASE_DIR, 'config/logging.json')

IS_REDACT_HEADER = True # If False, didsplay Authorization header content in screen and log. 


# Dictionary URLS 
# key: environment name
# value: API Host url
URLS = {
    'wheather_api' : 'https://weather.tsukumijima.net',
}

PATHS = {
    'FORECAST' : '/api/forecast'
}

HTTP_STATUS_OK = 200
HTTP_STATUS_CREATED = 201
HTTP_STATUS_NO_CONTENT = 204
HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_UNAUTHORIZED = 401
HTTP_STATUS_FORBIDDEN = 403
HTTP_STATUS_NOT_FOUND = 404
HTTP_STATUS_METHOD_NOT_ALLOWED = 405
HTTP_STATUS_UNPROCESSABLE_ENTITY = 422
HTTP_STATUS_TOO_MANY_REQUEST = 429
HTTP_STATUS_SERVER_ERROR = 500