def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Error: Dividing by zero is not allowed!"
    return num1 / num2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation to use: Addition, Subtraction, Multiplication, Division: ").lower()

if operation == "addition":
    print(addition(num1, num2))
elif operation == "subtraction":
    print(subtraction(num1, num2))
elif operation == "multiplication":
    print(multiplication(num1, num2))
elif operation == "division":
    print(division(num1, num2))
else:
    print("There was an error during operation selection, try again")                