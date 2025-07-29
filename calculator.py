#Operational functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#choose operand
operand = input("choose operation( +, -, /, * : ")

if operand == "+":
    result = add(num1, num2)
    print(f"sum is: {result}")
    
elif operand == "-":
    result = subtract(num1, num2)
    print(f"Subtraction is: {result}")
elif operand == "/":
    result = divide(num1, num2)
    print(f"Division is: {result}")
    
elif operand == "*":
    result = multiply(num1, num2)
    print(f"Multiplication is: {result}")
else:
    print("wrong operand")
    
    



