store = {}

class Breed:
    def __init__(self, name, milk_yield, gas_yield, feed_type, feed_price):
        self.name = name
        self.milk_yield = milk_yield
        self.gas_yield = gas_yield
        self.feed_type = feed_type
        self.feed_price = feed_price
        self.id = 1 
        self.store = store
        store['breed'] = self
        
    def get_pens(self, store):
        return [pen for pen in store['pens'] if pen.breed_id == self.id]
    
    def get_cows(self, store):
        return [cow for cow in store['cows'] if cow.breed_id == self.id]