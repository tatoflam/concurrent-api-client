from api_client.api_client import ApiClient
from api_client.formatter.weather_api import WheatherApiFormatter

apiclient = ApiClient( WheatherApiFormatter('wheather_api', 130010) )
url, headers, params, res_json, status = apiclient.get()