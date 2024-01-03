import requests
from drinksClient import DrinksClient
from receipt import Receipt

class ReceiptBuilder:
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
        self._request_api = DrinksClient()
        self._receipt_data = self._request_api.run()
        self._receipts = self.receipts_data_to_objects(self._receipt_data)
        return self._receipts
