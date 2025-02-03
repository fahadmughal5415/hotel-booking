import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype={"id": str})


#### Difference between class variables and instance variables
# Class variables are those that are inside of the class and 
# share inside of the whole class and we can access them by creating an 
# instance of the class and also access them by Class itself.
# Example
# class MyClass:
#   watermark = "CodeSeek" ----> Class variable
#   def __init__(self, name, value):
#       self.name = name ------> Instance variable
#       self.value = value ------> Instance variable


#### Differenctiate between class methods and instance methods
# Class methods are those that are inside of the class but they have
# the first parameter is cls and before of the class we wrote the 
# @classmethod. Instance methods are those that are inside of the class
# but they have the first parameter is self keyword and that's it.

#### What is properties
# Properties are behave like variables and by using the properties 
# we can modify the instance variables


#### What is the abstract method and abstract class
# Abstract class is that that cannot instantiated directly just because of its abstract method @abstractmethod. All of the other classes are inherited from that abstract class and all have the same method but different implementation.



class Hotel:
    watermark = "The real estate company"

    # instance method
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
    
    # class method
    @classmethod
    def get_total_hotels(cls):
        return len(df)
    

class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class DigitalTicket(Ticket):
    def generated(self):
        pass


class ReservationTicket(Ticket):

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
    def generate(self):
        content = f"""
    Thank you for the reservation.
    Here is your hotel details
    Customer Name: {self.the_customer_name}
    Hotel Name: {self.hotel.name}
"""
        return content
    

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    
hotel1 = Hotel(hotel_id=134)

print(hotel1.watermark)
print(Hotel.watermark)
print(hotel1.get_total_hotels)

reservation = ReservationTicket(customer_name="john smith  ", hotel_object=hotel1)

print(reservation.the_customer_name)
print(reservation.generate())
    

    

        


