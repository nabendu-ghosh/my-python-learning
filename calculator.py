calculator_logo = r'''
_____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

def addition(n1, n2):
    '''
    Takes two numbers and returns the sum
    '''
    return n1 + n2

def substraction(n1, n2):
    '''
    Takes two numbers and returns the difference
    '''
    return n1 - n2

def multiplication(n1, n2):
    '''
    Takes two numbers and returns the multplication
    '''
    return n1 * n2

def divide(n1, n2):
    '''
    Takes two numbers and returns the division
    '''
    if n1 == 0 and n2 == 0:
        return "Result is undefined"
    elif n2 == 0:
        return "Can not divide by 0"
    elif not isinstance(n1, int):
        return "Undefined"
    else:
        return n1 / n2
    
print(calculator_logo)

number1 = float(input("Please enter the first number: "))
operation = input('''
Please enter an operation.
"+" for Addition
"-" for Substraction
"*" for Multiplication
"/" for Divition
Pick an Operation: ''')
number2 = float(input("Please enter the second number: "))

if operation not in ["+", "-", "*", "/"]:
    final_output = "Invalid operation selected. Please select correct operation"
elif operation == "+":
    final_output = addition(number1, number2)
elif operation == "-":
    final_output = substraction(number1, number2)
elif operation == "*":
    final_output = multiplication(number1, number2)
elif operation == "/":
    final_output = divide(number1, number2)

print(f"{number1} {operation} {number2} = {final_output}")