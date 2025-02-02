import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        pass


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass


print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()

    name = input("Enter the name of the customer: ")
    reservation = ReservationTicket(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not available")