MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

def report():
    '''Prints a report of all available resources'''
    print(f"water = {resources['water']} ml,\n milk = {resources['milk']} ml,\n coffee = {resources['coffee']} ml, \n money = {resources['money']}")

def coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    pennies = int(input("How many pennies?: "))
    nickels = int(input("How many nickels?: "))
    total = quarters * 0.25 + dimes * 0.10 + pennies * 0.01 + nickels * 0.05
    return total

def latte_drink():
    '''function for latte drink'''
    if MENU['latte']['ingredients']['water'] <= resources['water'] and MENU['latte']['ingredients']['coffee'] <= resources['coffee'] and MENU['latte']['ingredients']['milk'] <= resources['milk']:
        result = coins()
        if MENU['latte']['cost'] <= result:
            print("Here's your latte enjoy !!")
            change = round(result - MENU['latte']['cost'], 2)
            print(f"Here's your change {change}")
            resources['water'] -= MENU['latte']['ingredients']['water']
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            resources['milk'] -= MENU['latte']['ingredients']['milk']
            resources['money'] += MENU['latte']['cost']


        else:
            print(f"Sorry, the amount you have entered is not sufficient, Here's your refund of {result}")
    else:
        print("Sorry there arent sufficient resources")

def cappuccino_drink():
    '''function for cappuccino_drink()'''
    if MENU['cappuccino']['ingredients']['water'] <= resources['water'] and MENU['cappuccino']['ingredients']['coffee'] <= resources['coffee'] and MENU['cappuccino']['ingredients']['milk'] <= resources['milk']:
        result = coins()
        if MENU['cappuccino']['cost'] <= result:
            print("Here's your cappuccino enjoy !!")
            change = round(result - MENU['cappuccino']['cost'], 2)
            print(f"Here's your change {change}")
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            resources['money'] += MENU['cappuccino']['cost']
        else:
            print(f"Sorry, the amount you have entered is not sufficient, Here's your refund of {result}")
    else:
        print("Sorry there arent sufficient resources")

def espresso_drink():
    '''function for espresso_drink()'''
    if MENU['espresso']['ingredients']['water'] <= resources['water'] and MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:
        result = coins()
        if MENU['espresso']['cost'] <= result:
            print("Here's your espresso enjoy !!")
            change = round(result - MENU['espresso']['cost'], 2)
            print(f"Here's your change {change}")
            resources['water'] -= MENU['espresso']['ingredients']['water']
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            resources['money'] += MENU['espresso']['cost']
        else:
            print(f"Sorry, the amount you have entered is not sufficient, Here's your refund of {result}")
    else:
        print("Sorry there arent sufficient resources")

def user_beverage():
    '''Takes input from the user and return the drink if all conditions satisfy'''
    machine_0n = True
    while machine_0n:
        beverage = input("Hello, What would you like to have? (espresso/latte/cappuccino): ").lower()
        if beverage == 'off':
            print("Bye Bye!!")
            machine_0n = False
        elif beverage == 'espresso':
            espresso_drink()
        elif beverage == 'latte':
            latte_drink()
        elif beverage == 'cappuccino':
            cappuccino_drink()
        elif beverage == 'report':
            report()


user_beverage()

