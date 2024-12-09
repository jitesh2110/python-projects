import os
import calculator_art

def add( num1 , num2 ):
    return num1 + num2

def subtract( num1 , nun2 ):
    return num1 - num2

def multiply( num1 , num2 ):
    return num1 * num2

def divide( num1 , num2 ):
    if num2 == 0:
        return "You can't divide by 0"
    return num1/num2

ope = {'+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}
def calculator():
    print(calculator_art.logo)
    print("This is calculator \n")
    num1 = float(input(("Enter the first number = ")))
    state = "y"
    while state == 'y':
        operation = input("Select the operation \n + \n - \n * \n / \n = ")
        num2 = float(input(("Enter the second number = ")))
        result = ope[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        state = input(f"Do you want to continue performing operations  on {result} ?'y' 'n' = ")
        if state == 'y':
            num1 = result
        else:
            os.system('clear')

            calculator()
calculator()    
