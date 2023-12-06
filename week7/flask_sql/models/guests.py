from store import store

class Guest:
    def __init__(self, name):
        self.name = name
        self.id = len(store['guests']) + 1
        store['guests'][self.id] = self

    def reservations(self):
        return [reservation for reservation in store['reservations'].values() if reservation.guest_id == self.id]
    
    def rooms(self):
        reservations_list = self.reservations()
        return [res.room for res in reservations_list]
    
    