import requests

class ApiClient:
    def __init__(self, URL):
        self.URL = URL

    def run(self, params = {}):
        response = requests.get(self.URL, params=params)
        return response.json()
    
# 1d15579652f94332888b4b368c03b876
    # d55038867d3d44f2a013f975bab86aa8