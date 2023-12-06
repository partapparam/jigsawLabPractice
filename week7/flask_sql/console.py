from models.guests import Guest
from models.reservations import Reservation
from models.rooms import Room
from store import store

guest = Guest('Param')
room1 = Room(1, 500)
room2 = Room(2, 400)
Reservation(guest, room1, 'tomoorw', 'after')
Reservation(guest, room2, 'tomoorw', 'after')
Reservation(guest, room1, 'yesterday', 'undecied')