class passenger:
    passenger_names = []
    total_weight = 46

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def weight_count(self):
        if self.weight > self.total_weight:
            print(f"{self.name} Too much weight!")
        else:
            print(f"{self.name} Carrying: {self.weight}")

penelope = passenger("penelope", 32)
david = passenger("david", 354)