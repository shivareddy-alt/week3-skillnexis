
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


calculator = Calculator()

try:
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = calculator.add(a, b)
    elif operator == "-":
        result = calculator.subtract(a, b)
    elif operator == "*":
        result = calculator.multiply(a, b)
    elif operator == "/":
        result = calculator.divide(a, b)
    else:
        raise ValueError("Invalid operator.")

    print("Result:", result)

except ValueError as error:
    print("Invalid input:", error)
except ZeroDivisionError as error:
    print("Error:", error)
