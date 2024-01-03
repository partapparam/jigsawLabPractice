import requests
from receipt import Receipt

class ReceiptBuilder:
    # fetch the receipts from the API
    def fetch_receipts(self):
        response = requests.get("https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE")
        restaurant_receipts = response.json()
        return restaurant_receipts
    
    # convert the receipts into Receipt Object Instances
    def create_receipt(self, receipt):
        return Receipt(**receipt)
    
    # go through data and generate list
    def receipts_data_to_objects(self, restaurant_receipts):
        receipts = []
        for receipt in restaurant_receipts:
            receipt_obj = self.create_receipt(**receipt)
            receipts.append(receipt_obj)
        return receipts
#   run the above methods and return the Receipt instances
    def run(self):
        self._receipt_data = self.fetch_receipts()
        self._receipts = self.receipts_data_to_objects(self._receipt_data)
        return self._receipts
