# Simple Calculator in Python

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input
operation = input("Enter choice (1/2/3/4): ")

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation and display the result
if operation == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input! Please choose a valid operation.")
