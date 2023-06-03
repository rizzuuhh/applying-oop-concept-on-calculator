import pyfiglet
import random

# Constructor: Initialize the title 
class Calculator:
    def __init__(self):
        self.title = "SIMPLE APP CALCULATOR"
        self.confetti = ["✨", "🎉"]

    # Print the title of the calculator 
    def print_title(self):
        title = pyfiglet.figlet_format("SIMPLE APP CALCULATOR", font = "banner3-D", width = 200 )
        print("\033[1;33m" + title)

    # Print the menu options for the calculator
    def print_menu(self):
        print("\033[1m\033[1;32mChoose an operation:")
        add = ("1 Addition (+)")
        add = pyfiglet.figlet_format("1 Addition (+)", font = "bulbhead",  width = 200 )
        print(add)


        sub = ("2 Subtraction (-)")
        sub = pyfiglet.figlet_format("2 Subtraction (-)", font = "bulbhead",  width = 200 )
        print(sub)
       
        mul = ("3 Multiplication (*)")
        mul = pyfiglet.figlet_format("3 Multiplication (*)", font = "bulbhead",  width = 200 )
        print(mul)


        div = ("4 Division (/)")
        div = pyfiglet.figlet_format("4 Division (/)", font = "bulbhead",  width = 200 )
        print(div)
       

    # Get user input with the provided message as prompt
    def get_user_input(self, message):
        return input(message)

    # Perform the specified operation on the given numbers
    def perform_operation(self, operation, num1, num2):
        if operation == '1':   # Addition
            return num1 + num2
        elif operation == '2': # Subtraction
            return num1 - num2 
        elif operation == '3': # Multiplication
            return num1 * num2
        elif operation == '4': # Division
            if num2 == 0:
                return "Error: Division by zero!"
            else:
                return num1 / num2
        else:
            return "Error: Invalid operation!"

    # Print the result of the calculation
    def print_result(self, result):
        if isinstance(result, float): # Check if the result is a float (for division)
            print("Result: {:.2f}".format(result))
        else:
            print("Result:", result)


    def print_confetti(self):
        confetti = " ".join(random.choices(self.confetti, k=10))
        print(confetti)

    # Run the calculator
    def run(self):
        self.print_title()
        repeat = True


        while repeat:
            self.print_menu() # Print the menu options
            operation = self.get_user_input("\033[0;35mEnter the operation number: ")  # Get the operation from the user
            num1 = float(self.get_user_input("Enter the first number: ")) # Get the first number from the user
            num2 = float(self.get_user_input("Enter the second number: ")) # Get the second number from the user

        # Get the operation from the user
            result = self.perform_operation(operation, num1, num2)
            self.print_result(result)
            print(result)  # Print the result


            choice = self.get_user_input("Do you want to try again? (y/n): ")
            repeat = (choice.lower() == 'y') # Ask if the user wants to repeat

    # Print the thank you message
        ty = ("THANK YOU")
        ty = pyfiglet.figlet_format("THANK YOU", font = "banner3-D", width = 200 ) 
        print("\033[1;33m" + ty)
        self.print_confetti()


# Create a new class called AdvancedCalculator that inherits from Calculator
class AdvancedCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def print_menu(self):
        super().print_menu()
        factorial = pyfiglet.figlet_format("5 Factorial (!)", font="bulbhead", width=200)
        print(factorial)

    def perform_operation(self, operation, num1, num2):
      if operation == '5':  # Factorial
        try:
            return self.factorial(num1)
        except ValueError:
            return "Error: Invalid input for factorial!"
        except Exception as e:
            return "Error: An exception occurred while calculating factorial: " + str(e)
      else:
        return super().perform_operation(operation, num1, num2)

# Create an instance of the AdvancedCalculator class
calculator = AdvancedCalculator()
# Run the calculator
calculator.run()