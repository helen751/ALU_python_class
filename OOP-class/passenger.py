class Passenger:
    def __init__(self):
        self.name = None
        self.current_location = None
        self.destination = None
        self.date = None
        self.details = {}

    def get_passenger_info(self):
        self.name = input("Enter your name: ")
        self.current_location = input("Enter your Current location: ")
        self.destination = input("Enter your destination: ")
        self.date = input("What is your travel date: ")

        self.details['name'] = self.name
        self.details['current_location'] = self.current_location
        self.details['destination'] = self.destination
        self.details['date'] = self.date
