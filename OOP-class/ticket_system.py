class TicketSystem:
    def __init__(self):
        welcome_message = "\tWelcome to Ticket System\n"
        print(welcome_message)

    def get_user_details(self):
        self.name = (input("What is your name? "))
        self.age = int(input("What is your age? "))
        self.origin = input("Where are you departing from? ")
        self.destination = input("Where are you departing to? ")

    def choose_type(self):
        print("Select your ticket type \n "
                       "1] First Class \n 2] Economy")
        t_type = int(input("Choose now: "))
        if t_type == 1:
            self.ticket_type = "First Class"
        else:
            self.ticket_type = "Economy"
        return self.ticket_type

    def first_class(self):
        self.weight = (input("What is the total weight? "))

    def booking_confirmation(self):
        print("Thank you for your ticket! \n\n")
        print("Here are your ticket details:")
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Origin: " + self.origin)
        print("Destination: " + self.destination)

        if self.ticket_type == "Economy":
            print("Weight not allowed!")
            print("Your ticket will be in Economy.")
        else:
            print("Weight: " + self.weight + "KG")
            print("Your ticket will be in First Class.")

#System logic
def main():
    ticket_system = TicketSystem()
    ticket_system.get_user_details()

    if ticket_system.choose_type() == "First Class":
        ticket_system.first_class()

    ticket_system.booking_confirmation()

main()