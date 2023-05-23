# Constructor: Initialize the title 
class Calculator:
    def __init__(self):
        self.title = "SIMPLE APP CALCULATOR"
    # Print the title of the calculator 
    def print_title(self):
        print(self.title)
    
    # Print the menu options for the calculator
    def print_menu(self):
        print("Choose an operation:")
        print("1 Addition (+)")
        print("2 Subtraction (-)")
        print("3 Multiplication (*)")
        print("4 Division (/)")
    
    # Get user input with the provided message as prompt
        def get_user_input(self, message):
            return input(message)
       
    # Perform the specified operation on the given numbers
        def perform_operation(self, operation, num1, num2):
            if operation == '1':  # Addition
                return num1 + num2
            elif operation == '2':  # Subtraction
                return num1 - num2
            elif operation == '3':  # Multiplication
                return num1 * num2
            elif operation == '4':  # Division
                if num2 == 0:
                    return "Error: Division by zero!"
                else:
                    return num1 / num2
            else:
                return "Error: Invalid operation!"
    # Print the result of the calculation
    def print_result(self, result):
        if isinstance(result, float):  # Check if the result is a float (for division)
            print("Result: {:.2f}".format(result))
        else:
            print("Result:", result)
    # Run the calculator
    def run(self):
        self.print_title() 
        repeat = True

    
        while repeat:
            self.print_menu()  # Print the menu options
            operation = self.get_user_input("Enter the operation number: ")  # Get the operation from the user
            num1 = float(self.get_user_input("Enter the first number: "))  # Get the first number from the user
            num2 = float(self.get_user_input("Enter the second number: "))  # Get the second number from the user
    # Perform the operation
        result = self.perform_operation(operation, num1, num2)  
        self.print_result(result)  # Print the result
    # Get the operation from the user
        choice = self.get_user_input("Do you want to try again? (y/n): ")  # Ask if the user wants to repeat
        repeat = (choice.lower() == 'y')
    # Print the thank you message
    print("THANK YOU")  

# Create an instance of the Calculator class
# Run the calculator
