import passenger
from EconomyClass import EconomyPassenger
from FirstClass import FirstClassPassenger
from PremiumClass import PremiumClassPassenger
import sqlite3



def final_details(det):
    print("\n\tRegistration Completed! Here are your details")

    for key, item in det.items():
        print(f"{key}: {item}")

print("\tWelcome to Ticket System\n")
print("Select your ticket type: "
                   "\n\t1] Economy Class"
                   "\n\t2] First Class \n\t3] Premium Class"
                   "\n\t0] Exit")
choose = int(input("Choose now: "))

if choose == 1:
    economy = EconomyPassenger()
    economy.get_passenger_info()
    final_details(economy.details)

elif choose == 2:
    first = FirstClassPassenger()
    first.get_passenger_info()
    first.set_weight()
    first.access_lounge()
    final_details(first.details)

elif choose == 3:
    type = PremiumClassPassenger()
    type.get_passenger_info()
    type.set_weight()
    type.get_priority_boarding()
    final_details(type.details)

else:
    exit(1)


