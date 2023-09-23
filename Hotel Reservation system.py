#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Room:
    def __init__(self, room_number, room_type, is_reserved=False, is_occupied=False):
        self.room_number = room_number
        self.room_type = room_type
        self.is_reserved = is_reserved
        self.is_occupied = is_occupied

class HotelReservationSystem:
    def __init__(self):
        self.rooms = []
        self.reservations = []
        self.Reservation_ID = 1

    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        self.rooms.append(room)


    def find_available_room(self, room_type, check_in, check_out):
        for room in self.rooms:
            if room.room_type == room_type and not room.is_reserved and not room.is_occupied:
                return room
        return None

    def create_reservation(self, guest_name, room_type, check_in, check_out):
        room = self.find_available_room(room_type, check_in, check_out)
        if room:
            reservation_id = self.Reservation_ID
            self.Reservation_ID += 1
            reservation = {
                'reservation_id': reservation_id,
                'guest_name': guest_name,
                'room': room,
                'check_in': check_in,
                'check_out': check_out
            }
            self.reservations.append(reservation)
            room.is_reserved = True
            print(f'Reservation created. Reservation ID: {reservation_id}')
        else:
            print('No available rooms of the requested type.')

    def check_out(self, reservation_id):
        for reservation in self.reservations:
            if reservation['reservation_id'] == reservation_id:
                reservation['room'].is_reserved = False
                reservation['room'].is_occupied = False
                self.reservations.remove(reservation)
                print('Check-out successful.')
                return
        print('Invalid reservation ID.')

    def calculate_total_cost(self, room, check_in, check_out):
    # calculate your own cost calculation here based on room rates, additional services, and taxes
        return 0

# Example usage
hotel = HotelReservationSystem()

# Add rooms
hotel.add_room('101', 'Single')
hotel.add_room('102', 'Double')
hotel.add_room('103', 'Triple')

# Create a reservation
hotel.create_reservation('Tyler Durden','Single','21 may','23 may')
hotel.create_reservation('Walter White','Single','21 may','27 may')


# In[ ]:




