import requests
from receipt import Receipt

def run():
    receipts = []
    response = requests.get("https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE")
    restaurant_receipts = response.json()
    for receipt in restaurant_receipts:
        receipt_obj = Receipt(**receipt)
        receipts.append(receipt_obj)

    return receipts