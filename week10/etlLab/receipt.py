class Receipt:
    attributes = ['obligation_end_date_yyyymmdd', 'location_name', 'liquor_receipts', 'wine_receipts', 'beer_receipts']

    def __init__(self, **kwargs):
        for key, v in kwargs.items():
            if key in self.attributes:
                setattr(self, key, v)

    