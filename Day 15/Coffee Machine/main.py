print("This is coffee machine \n")
from data import resources
from data import MENU
def report():
    print(f"Water = {resources['water']}\nMilk = {resources['milk']}\nCoffee = {resources['coffee']}\n")

def make(water, milk, coffee ):
    resources['water']-= water
    resources['milk'] -= milk
    resources['water'] -= coffee


def stock( water, milk, coffee ):
    if resources['water'] < water:
        return 'water'
    elif resources['milk'] < milk:
        return 'milk'
    elif resources['coffee'] < coffee:
        return 'coffee'
    else:
        return 'available'

def bill(name):
    rupee = int(input("Enter the amount in rupees = "))
    if name == 'espresso' and rupee >= MENU['espresso']['cost']:
        rupee -= MENU['espresso']['cost']
    elif name == 'latte' and rupee >= MENU['latte']['cost']:
        rupee -= MENU["latte"]['cost']
    elif name == 'cappuccino' and rupee >= MENU['cappuccino']['cost']:
        rupee -= MENU['cappuccino']['cost']
    else:
        return False
    print(f"Here is Rupee {rupee} in change")
    return True


def order():
    name = input("What would you like? ( espresso / latte / cappuccino ) = ").lower()
    return name

def coffeemachine():
    name =order()
    if name == 'espresso':
        status = stock(50 , 0, 18)
        if status == 'available':
            change = bill(name)
            if change == False:
                return 'Sorry that is not enough money, Money refunded'
            else:
                make(50,0,18)
                print("Here is your espresso Enjoy!")
        else:
            return f'Sorry there is not enough {status}'

    elif name == 'latte':
        status = stock(200 , 150, 24)
        if status == 'available':
            change = bill(name)
            if change == False:
                return 'Sorry that is not enough money, Money refunded'
            else:
                make(200,150,24)
                print("Here is your latte Enjoy!")
        else:
            return f'Sorry there is not enough {status}'

    elif name == 'cappuccino':
        status = stock(250 , 100, 24)
        if status == 'available':
            change = bill(name)
            if change == False:
                return 'Sorry that is not enough money, Money refunded'
            else:
                make(250,100,24)
                print("Here is your cappuccino Enjoy!")
        else:
            return f'Sorry there is not enough {status}'

    else:
        return 'Please enter valid choice'


print(coffeemachine())

