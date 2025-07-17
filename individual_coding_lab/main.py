from assignment import Assignment #importing the assignment file.
import gradeCalculator #importing the grade calculator file
import colored_print_message #importing the colord message file

#creating one instance of the assignment class to use
assignment = Assignment()

#instance of the colored message class
colored_message = colored_print_message.ColoredMessage()

#instance of the grade calculator class
grade_calculator = gradeCalculator.GradeCalculator()

#the main class that starts the application and controls the flow
def main():
    colored_message.print("\n\n\tWELCOME TO HELEN'S GRADE CALCULATOR", "blue")
    option_menu()

#creating an option menu function for good organisation of my app.
def option_menu():
    print(
        "What would you like to do now? \n1] Add new assignment \n2] Remove existing assignment \n3] Calculate Grades \n0] Exit")
    choose = input("Select a valid option: ")

    #based on user selection, calling the required classes
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
        colored_message.print("\nThank you for using this App! See you next time!\n\n", "blue")
        exit(0)

#calling the main function to start the application
main();