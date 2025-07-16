from assignment import Assignment
import colored_print_message

class GradeCalculator:
    def __init__(self):
        # creating an instance of the colored print message class
        self.colored_message = colored_print_message.ColoredMessage()
        self.assignments_dict = {}
        self.total_assignment_calculation = {}
        self.gpa_scale = 5
        self.total_GPA = None

    #The final function to display the grades and assignment details.
    def display_grade_total(self):

        # Printing table header with column lines
        self.colored_message.print("\n\t\t\t ====YOUR ALU TRANSCRIPT====", "blue")
        print(
            f"| {'Assignment Name':<20} | {'Category':<10} | {'Grade (%)':<10} | {'Weight (%)':<11} | {'Final Grade':<12} |")
        print("|" + "-" * 22 + "|" + "-" * 12 + "|" + "-" * 12 + "|" + "-" * 13 + "|" + "-" * 14 + "|")

        #getting the total grade percent for each category and checking if the student passed or failed
        formative_percent = (self.total_assignment_calculation['formative'] / 60) * 100
        summative_percent = (self.total_assignment_calculation['summative'] / 40) * 100

        if formative_percent >= 50 and summative_percent >= 50:
            verdict = "PASS"

        else:
            verdict = "FAIL"

        #looping through the assignments dictionary and printing their details in a table form
        for category, assignments in self.assignments_dict.items():
            for assignment in assignments:
                print(
                    f"| {assignment['assignment_name']:<20} | {category.upper():<10} | {assignment['grade']:<10} | {assignment['weight_in_per']:<11} | {round(assignment['total_grade'], 2):<12} |")

        formative_total = round(self.total_assignment_calculation['formative'],2)
        summative_total = round(self.total_assignment_calculation['summative'],2)

        #adding an extra row and column line to make the output more organised
        print("|" + "-" * 22 + "|" + "-" * 51 + "|")

        if formative_percent >= 50:
            print(
                f"| {'Formatives (60)':<60} | {f'{formative_total} [{round(formative_percent)}%]':<12} |"
            )

        else:
            self.colored_message.print(f"| {'Formatives (60)':<60} | {f'{formative_total} [{round(formative_percent)}%]':<12} |", "red")

        #displaying summative total in different color depending on if student passed or failed
        if summative_percent >= 50:
            print(
            f"| {'Summatives (40)':<60} | {f'{summative_total} [{round(summative_percent)}%]':<12} |")

        else:
            self.colored_message.print(f"| {'Summatives (40)':<60} | {f'{summative_total} [{round(summative_percent)}%]':<12} |", "red")

        #displaying the fina verdict if user passed both formatives and summative
        #Shows in Red when user fails and also display the gpa in RED
        print("|" + "-" * 22 + "|" + "-" * 51 + "|")

        if verdict == "PASS":
            self.colored_message.print(f"| {'GPA':<60} | {round(self.total_GPA, 3):<12} |", "green")
            self.colored_message.print("\n\t\tSUMMARY", "blue")
            self.colored_message.print("You scored more than 50% in both summative and formatives"
                                       "\n Hence, you PASSED this course!", "green")

        else:
            self.colored_message.print(f"| {'GPA':<60} | {round(self.total_GPA, 3):<12} |", "red")
            self.colored_message.print("\n\t\tSUMMARY", "blue")
            if formative_percent < 50 and summative_percent < 50:
                self.colored_message.print("You scored LESS than 50% in both summative and formatives,"
                                           "\n Hence, you FAILED and will REPEAT this course!", "red")

            elif summative_percent < 50 and formative_percent >= 50:
                self.colored_message.print("You scored less than 50% in the summative "
                                       "\n Hence, you FAILED and will REPEAT this course!", "red")

            else:
                self.colored_message.print("You scored less than 50% in the formative "
                                           "\n Hence, you FAILED and will REPEAT this course!", "red")
        print()


    #function to calculate the GPA based on the grades
    def calculate_gpa(self):
        gpa = 0
        #looping to get each category total grades in the dictionary
        for each_category_grade in self.total_assignment_calculation.values():
            gpa += float(each_category_grade)

        #calculating the gpa with the formula
        self.total_GPA = (gpa / 100) * self.gpa_scale
        #appending the gpa to the grades dictionary
        self.total_assignment_calculation["GPA"] = self.total_GPA

        #calling the final function to display grade details and summary
        self.display_grade_total()


    #function to calculate the total grades obtained in each category
    def calculate_each_category_grade(self, assignments_dict):
        self.assignments_dict = assignments_dict

        #looping through the dictionary categories
        for category, each_assignment in self.assignments_dict.items():
            i = 0;
            category_grade = 0

            #looping through all items in each category and adding the total grades
            while i < len(each_assignment):
                category_grade += each_assignment[i]["total_grade"]

                i = i + 1

            #updating the dictionary that stores students final grades
            self.total_assignment_calculation[category] = category_grade

        #calling the function to calculate student's gpa
        self.calculate_gpa()


    def calculate_each_grade(self, assignments_dict):
        #calculating the total grade for each assignment in the dictionary
        #formula = (assignment_grade * assignment_weight) / 100
        self.assignments_dict = assignments_dict
        no_assignments = True

        #looping through the dictionary to calculate the total grade of each assignment
        for each_assignment in self.assignments_dict.values():
            i = 0;

            #checking if there is no assignment added yet
            if len(each_assignment) != 0:
                no_assignments = False

                #looping through each category, formative and summative and calculating the total grades.
                while i<len(each_assignment):
                    each_assignment_grade = each_assignment[i]["grade"]
                    each_assignment_weight = each_assignment[i]["weight_in_per"]
                    total_grade = (each_assignment_grade * each_assignment_weight) / 100
                    each_assignment[i]["total_grade"] = total_grade

                    i = i+1

        if no_assignments:
            self.colored_message.print("No Assignments Found!\nPlease add an assignment first.", "red")

        else:
            #calling the function to calculate the total grades in each category
            self.calculate_each_category_grade(self.assignments_dict)




