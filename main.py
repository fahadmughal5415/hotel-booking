import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
    Thank you for the reservation.
    Here is your hotel details
    Customer Name: {self.customer_name}
    Hotel Name: {self.hotel.name}
"""
        return content
    

class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
    
    def validate(self, expiration, holder, cvv):
        # Implement your credit card validation logic here
        self.expiration = expiration
        self.holder = holder
        self.cvv = cvv
        card_data = {"number": self.card_number, "expiration": self.expiration, "holder": self.holder, "cvv": self.cvv}

        if card_data in df_cards:
            return True
        else:
            return False
        


print(df)
print(df_cards)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    number = input("Enter the credit card number: ")
    expiration = input("Enter the expiration date (MM/YY): ")
    holder = input("Enter the credit card holder's name: ")
    cvv = input("Enter the CVV: ")
    credit_card = CreditCard(number)
    if credit_card.validate(expiration, holder, cvv):
        hotel.book()
        name = input("Enter the name of the customer: ")
        reservation = ReservationTicket(name, hotel)
        print(reservation.generate())
    else:
        print("Invalid credit card details")
else:
    print("Hotel is not available")