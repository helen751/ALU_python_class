import colored_print_message

#class that handles all the assignment functions
class Assignment:

    #creating the constructor method for the class.
    def __init__(self):
        #defining all the class variables in the constructor.
        self.assignment_name = None
        self.assignment_category = None
        self.assignment_weight = None
        self.assignment_grade = None

        #setting the total weight allocated for all summative and formatives
        self.max_formative_total_weight = 60
        self.max_summative_total_weight = 40

        #creating an instance of the colored print message class
        self.colored_message = colored_print_message.ColoredMessage()

        #dictionary that stores all the assignments in formative and summative category
        self.assignments_dict = {"formative":[], "summative":[]}

    #creating a function to search if an assignment name exists in the dictionary
    def search_assignment(self, search_assignment_name):
        found = False
        found_id = None
        found_category = None

        #looping through the assignments dictionary and matching each name to the name being searched for
        for category in ["formative", "summative"]:
            i = 0
            while i < len(self.assignments_dict[category]):
                assignment = self.assignments_dict[category][i]
                #matching each assignment name with the name being searched for
                if assignment["assignment_name"].lower() == search_assignment_name.lower():
                    found = True
                    found_category = category
                    found_id = i

                i += 1  # loop increment

            if found:
                break  # break out of the for loop

        if not found:
            found_id = None

        #returning the category where the name was found and its list ID to be used for deletion
        return {"category": found_category, "index": found_id}


    #function to check whether the summative or formative has exceeded the total allocated weight
    def check_remaining_weight(self, category, new_weight):

        # Set max allowed weight based on category
        if category == "formative":
            max_weight = self.max_formative_total_weight
        else:
            max_weight = self.max_summative_total_weight

        # Sum current weights of all formative or summative in the dictionary
        current_weight = sum(a["weight_in_per"] for a in self.assignments_dict[category])
        remaining = max_weight - current_weight

        #checking if the new weight entered is a negative number
        if remaining < 0:
            self.colored_message.colored("NEGATIVE numbers are not allowed as weight", "red")
            return False

        #checking if the new weight is 0
        if remaining == 0:
            self.colored_message.print("Note: This assignment will not count for your total final grades", "yellow")

        # checking if category weight limit has been reached.
        elif remaining == 0 and new_weight > 0:
            self.colored_message.print("Total Assignment Weight Limit reached for " + category.upper(), "red")
            return False

        # Check if new_weight will exceed the allowed total
        elif new_weight > remaining:
            self.colored_message.print(
                f"You only have {remaining}% remaining weight for {category.upper()} assignments.", "red"
            )
            return False

        return True


    #creating a method that handles adding new assignments
    def add_new_assignment(self):
        #clearing the console for a well organised program flow

        print("\n\tAdding new assignment...")
        #initialising all the variables with the correct input from the user
        self.assignment_name = input("Enter new assignment name: ")
        if self.assignment_name == "":
            self.colored_message.print("Assignment Name cannot be empty!.", "red")
            return #stop here and handle this error.

        assignment_category_option = input("1] Formative (FA) "
                                           "\n2] Summative [SA]"
                                           "\nChoose the assignment category(1 or 2):")

        #checking if the user selected either 1 or 2 (formative/summative) only.
        allowed_weight = None
        if assignment_category_option == "1":
            self.assignment_category = "formative"
            allowed_weight = "60"

        elif assignment_category_option == "2":
            self.assignment_category = "summative"
            allowed_weight = "40"

        else:
            self.colored_message.print("Invalid choice.", "red")
            return #stop the program and handle this error

        #asking the user to enter the assignment weight and checking if it is a number.
        try:
            self.assignment_weight = float(input("Enter assignment weight(out of "+allowed_weight+"): "))
        except ValueError:
            self.colored_message.print("The Assignment weight must be a number.", "red")
            return  # stop the program and handle this error

        #checking if the user entered a valid assignment weight from 0 to the total weight allowed
        if not self.check_remaining_weight(self.assignment_category, self.assignment_weight):
            return  # stop the program and handle this error

        # asking the user to enter their grade and checking if it is a number
        try:
            self.assignment_grade = float(input("Enter assignment grade: "))
        except ValueError:
            self.colored_message.print("The Assignment grade must be a number.", "red")
            return  # stop the program and handle this error

        #checking if the user entered a valid grade from 0-100
        if self.assignment_grade < 0 or self.assignment_grade > 100:
            self.colored_message.print("The Assignment grade must be from 0 - 100.", "red")
            return  # stop the program and handle this error

        #if all checks are passed and user entered correct assignment details
        #input them as a dictionary under summative or formative category in the parent dictionary
        new_assignment = {
            "assignment_name": self.assignment_name,
            "weight_in_per": self.assignment_weight,
            "grade": self.assignment_grade
        }
        # Appending it to the right category
        self.assignments_dict[self.assignment_category].append(new_assignment)

        #user-friendly message
        self.colored_message.print("The Assignment has been added Successfully.", "green");


    #creating a function to delete an assignment from the dictionary
    def delete_assignment(self):
        print("\n\tDeleting assignment...")

        #getting the name of the assignment to delete
        del_assignment_name = input("Enter the name of the assignment to delete: ")

        #calling the search assignment function to check if the assignment exist in the dictionary.
        search_assignment = self.search_assignment(del_assignment_name)

        #if the assignment name does not exist
        if search_assignment["index"] is None:
            self.colored_message.print("The assignment name does not exist.", "red")
            return

        #if the assignment exist, show a proper message to the user
        else:
            category = search_assignment["category"]
            index = int(search_assignment["index"])
            self.colored_message.print("Found assignment: " + del_assignment_name + " in " + category.upper(), "blue")

        #asking the user to confirm if they still want to delete the assignment or not
        confirm = input("\nDo you want to delete it? (yes/no): ").strip().lower()

        if confirm.lower == "yes" or confirm.lower() == "y":
            del self.assignments_dict[category][index]
            self.colored_message.print("Assignment: "+ del_assignment_name + " deleted from " + category.upper(), "green")
        else:
            self.colored_message.print("Deletion cancelled.", "yellow")

