# To fix the DIP issue, I created an HttpService interface so that 
# the Http class can work with any service that implements this interface. 
# This way, I can easily swap out different service implementations without changing the Http class, 
# making the code more flexible and easier to maintain.

from abc import ABC, abstractmethod
import requests

class HttpService(ABC):
    @abstractmethod
    def request(self, url: str, method: str, options: dict = None):
        pass

class XMLHttpService(HttpService):
    def request(self, url: str, method: str, options: dict = None):
        if method == 'GET':
            response = requests.get(url, params=options)
        elif method == 'POST':
            response = requests.post(url, data=options)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        return response.text

class Http:
    def __init__(self, service: HttpService):
        self._service = service

    def get(self, url: str, options: dict = None):
        self._service.request(url, 'GET', options)

    def post(self, url: str, options: dict = None):
        self._service.request(url, 'POST', options)

# Example usage
service = XMLHttpService()
http = Http(service)
http.get("http://website.com", {"param": "value"})
http.post("http://website.com", {"param": "value"})
