import sys

def jama(num1, num2):
    return num1 + num2

def manfi(num1, num2):
    return num1 - num2

def zarab(num1, num2):
    return num1 * num2

def taqsim(num1, num2):
    return num1 / num2

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "jama":
    output = jama(num1, num2)
elif operation == "manfi":
    output = manfi(num1, num2)
elif operation == "zarab":
    output = zarab(num1, num2)
elif operation == "taqsim":
    output = taqsim(num1, num2)
else:
    output = "Invalid Operation"
print(output)
