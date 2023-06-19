"""
The program allows to do a simple calculation which takes two arguments
"""

class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # add function
    def add(self):
        return self.num1 + self.num2

    # subtract function
    def subtract(self):
        return self.num1 - self.num2

    # multiple function
    def multiply(self):
        return self.num1 * self.num2

    # Division function
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by 0"

    # Modulo function
    def mod(self):
        return self.num1 % self.num2

while True:
    choice = int(input("""
1. addition
2. subtraction
3. multiplication
4. division
5. modulo
: """))
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))

    calculator = Calculator(a, b)

    if choice == 1:
        print(f"{a} + {b} = {calculator.add()}")
    elif choice == 2:
        print(f"{a} - {b} = {calculator.subtract()}")
    elif choice == 3:
        print(f"{a} * {b} = {calculator.multiply()}")
    elif choice == 4:
        print(f"{a} / {b} = {calculator.divide()}")
    elif choice == 5:
        print(f"{a} % {b} = {calculator.mod()}")

    next = input("Continue? (yes/no): ").lower()
    if next == "no":
        break
