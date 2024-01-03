import requests

class ApiClient:
    def __init__(self, URL):
        self.URL = URL

    def run(self, params = {}):
        response = requests.get(self.URL, params=params)
        return response.json()