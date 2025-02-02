class Hotel:
    def __init__(self, id):
        pass
    def book(self):
        pass

    def available(self):
        pass

    def book(self):
        pass


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass


id = input("Enter the id of the hotel")
hotel = Hotel(id)
if hotel.available():
    hotel.book()

name = input("Enter the name of the customer: ")
reservation = ReservationTicket(name, hotel)
reservation.generate()