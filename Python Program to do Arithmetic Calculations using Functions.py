#Python Program to do Arithmetic Calculations using Functions

# function to add two numbers
def add(a, b):
    return a + b

# function to subtract two numbers
def subtract(a, b):
    return a - b

# function to multiply two numbers
def multiply(a, b):
    return a * b

# function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

# taking input from user
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

# Calling functions and displaying results
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

