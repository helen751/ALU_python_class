from assignment import Assignment #importing the assignment file.
import gradeCalculator #importing the grade calculator file
import colored_print_message

#creating one instance of the assignment class to use
assignment = Assignment()
colored_message = colored_print_message.ColoredMessage()
grade_calculator = gradeCalculator.GradeCalculator()

#the main class that starts the application
def main():
    print("\tWELCOME TO HELEN'S GRADE CALCULATOR")
    option_menu()

#creating an option menu function for good organisation of my app.
def option_menu():
    print(
        "What would you like to do now? \n1] Add new assignment \n2] Remove existing assignment \n3] Calculate Grades \n0] Exit")
    choose = input("Select a valid option: ")

    if choose == "1":
        assignment.add_new_assignment()
        print()
        option_menu()

    elif choose == "2":
        assignment.delete_assignment()
        print()
        option_menu()

    elif choose == "3":
        grade_calculator.calculate_each_grade(assignment.assignments_dict)
        print()
        option_menu()
    else:
        colored_message.print("Thank you for using this App! See you next time!", "yellow")
        exit(0)


main();