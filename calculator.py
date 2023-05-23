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
    # Check if the result is a float (for division)
    # Run the calculator
    # Print the menu options
    # Get the operation from the user
    # Get the first number from the user
    # Get the second number from the user
    # Perform the operation
    # Print the result
    # Ask if the user wants to repeat
    # Print the thank you message
# Create an instance of the Calculator class
# Run the calculator
