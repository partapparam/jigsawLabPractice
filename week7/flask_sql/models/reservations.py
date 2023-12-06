from store import store

class Reservation:
    def __init__(self, guest, room, start_day, end_day):
        self.start_day = start_day
        self.end_day = end_day
        self.room = room
        if self.room:
            self.room_id = room.id
        self.guest = guest
        if self.guest:
            self.guest_id = guest.id 
        self.id = len(store['reservations']) + 1
        store['reservations'][self.id] = self