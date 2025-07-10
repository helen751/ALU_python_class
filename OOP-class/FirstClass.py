from passenger import Passenger
from random import randint

class FirstClassPassenger(Passenger):
    def __init__(self):
        super().__init__()

    def set_weight(self):
        self.weight = input("Enter the total weight: ")
        self.details.update({'weight': self.weight})


    def access_lounge(self):
        self.lounge_access = randint(1, 100)
        self.details.update({'lounge_access': self.lounge_access})