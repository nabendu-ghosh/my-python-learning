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
}

machine_power = "on"
money = 0

def report_resources():
    global resources
    global money
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"money: {money}")

def check_resources(drink: str):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def make_drink(drink: str):
    global money
    for ingredient in MENU[drink]["ingredients"]:        
        resources[ingredient] = resources[ingredient] - MENU[drink]["ingredients"][ingredient]
    money += MENU[drink]["cost"]
    print(f"Here is your {drink} ☕")

def transaction(drink: str):
    print(f"Cost of your drink: ${MENU[drink]["cost"]}")
    print("Please insert coins: ")
    quarters = int(input("No of of quarters: "))
    dimes = int(input("No of of dimes: "))
    nickels = int(input("No of of nickels: "))
    pennies = int(input("No of of pennies: "))

    inserted_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    actual_cost = MENU[drink]["cost"]
    print(f"You have inserted: ${inserted_money}")

    if inserted_money == actual_cost:
        print("Transaction successful")
        return True
    elif inserted_money > actual_cost:
        change = round(inserted_money - actual_cost, 2)
        print(f"Here is ${change} dollars in change.")
        print("Transaction successful")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

while machine_power == 'on':
    users_choice = input("Good day! What would you like to drink? " \
    "Type 'espresso', 'latte' or 'cappuccino': ").lower()

    if users_choice == "off":
        machine_power = "off"
        print("Switching off coffee machine for maintenance")
    elif users_choice == "report":
        report_resources()
    elif users_choice in ["espresso", "latte", "cappuccino"]:
        resource_status = check_resources(users_choice)
        if resource_status:
            transaction_status = transaction(users_choice)
            if transaction_status:
                make_drink(users_choice)
    else:
        print("Please enter a valid command")

