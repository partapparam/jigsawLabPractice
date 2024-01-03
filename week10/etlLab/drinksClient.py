import requests

class DrinksClient:
    URL = "https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE"
    # fetch the receipts from the API
    def run(self):
        response = requests.get(self.URL)
        return response.json()
    

class TexasDrinksAPI:
    ROOT_URL = "https://data.texas.gov/resource/naix-2893.json"
    # we can refactor further by updating the how we fetch different resources from our API in the run method. 
    def run(self, params = {'location_name': 'HYATT HOUSE DALLAS/UPTOWN'}):
        response = requests.get(self.ROOT_URL, params)
        return response.json()