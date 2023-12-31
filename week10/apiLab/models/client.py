import requests

class ApiClient:
    def __init__(self, URL: str) -> None:
        self.URL: str = URL

    def run(self, params = {}) -> dict:
        response = requests.get(url=self.URL, params=params)
        return response.json()
    
# 1d15579652f94332888b4b368c03b876
    # d55038867d3d44f2a013f975bab86aa8