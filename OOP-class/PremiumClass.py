from passenger import Passenger

class PremiumClassPassenger(Passenger):
    def __init__(self):
        super().__init__()

    def set_weight(self):
        weight = input("Enter the total weight: ")
        self.details.update({"weight": weight})

    def get_priority_boarding(self):
        priority_boarding = True
        self.details.update({"priority_boarding": priority_boarding})