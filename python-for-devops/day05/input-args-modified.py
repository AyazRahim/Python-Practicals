import sys

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
    output = addition(num1, num2)
elif operation == "subtraction":
    output = subtraction(num1, num2)
elif operation == "multiplication":
    output = multiplication(num1, num2)
elif operation == "division":
    output = division(num1, num2)
else:
    output = "Invalid operation"

print(output)
