from store import store

class Room:
    def __init__(self, room_number, rate):
        self.room_number = room_number
        self.rate = rate
        self.id = len(store['rooms']) + 1
        store['rooms'][self.id] = self

    def reservations(self):
        return [reservation for reservation in store['reservations'].values() if reservation.room_id == self.id]