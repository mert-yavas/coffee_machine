from resource_and_settings import MENU , resources
import sys

full_water = resources['water']
full_coffee = resources['coffee']
full_milk = resources['milk']   
money = 0   

      
def coffee_machine(menu, coffee_type):
    '''The main flow of our coffee machine is based on this function.'''
    global full_water, full_coffee, full_milk, money
    coffee_machine_working = True
    while coffee_machine_working:
        select_coffee = ask()
        if select_coffee == 'report':
            coffee_machine_report()
            continue
        if select_coffee == 'off':
            sys.exit()
        else:
            water, coffee, milk ,cost = coffee_ingredients(MENU, select_coffee)
            waterisFull, coffeeisFull , milkisFull = check_resources(water, coffee, milk)
            if waterisFull < 0 :
                print("Sorry there is not enough water.")
                coffee_machine_working = True
            elif coffeeisFull < 0:
                print("Sorry there is not enough coffee.")
                coffee_machine_working = True
            elif milkisFull < 0 :
                print("Sorry there is not enough milk.")
                coffee_machine_working = True
            else:
                print('Please insert coins.')
                change = check_change(MENU, select_coffee)
                if change < 0:
                    print("Sorry that's not enough money. Money refunded.")
                    coffee_machine_working = False
                else:
                    print(f' Here is ${change:.2f} in change.')
                    print(f' Here is your {select_coffee} ☕️. Enjoy!')
                    full_water -= water
                    full_coffee -= coffee
                    full_milk -= milk
                    money += cost
                    continue


def coffee_ingredients(menu , coffee_type):
    '''Determines the amount of resources spent according to coffee types'''
    ingredients = menu[coffee_type]['ingredients']
    cost = menu[coffee_type]['cost']
    
    water = ingredients.get('water', 0)
    coffee = ingredients.get('coffee', 0)
    milk = ingredients.get('milk', 0)
    return water , coffee, milk, cost


def get_coins(coin_name, coin_value):
    '''It asks the user how many coins to add. It subtracts the total according 
    to the coin types. If there is an entry other than an integer, it gives 
    a ValueError error and asks for the number of coins to be entered again.'''
    while True:
        try:
            number_of_coins = int(input(f'How many {coin_name}?: '))
            return number_of_coins * coin_value
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        
def calculate_total_coin():
    '''Determines the coin values and subtracts the sum of all coins.'''
    total_quarter = get_coins('quarter', 0.25)
    total_dimes = get_coins('dimes', 0.10)
    total_nickles = get_coins('nickles', 0.05)
    total_pennies = get_coins('pennies', 0.01)
    total_coins = total_quarter + total_dimes + total_nickles + total_pennies
    return total_coins

def check_resources(water, coffee, milk):
    '''Detects the state of its resources within the machine.'''
    check_water = full_water - water
    check_cofee = full_coffee - coffee
    check_milk = full_milk - milk
    return check_water, check_cofee , check_milk

def check_change(menu, coffee_type):
    '''Calculates the change of the money paid'''
    payment = calculate_total_coin()
    _, _, _, cost = coffee_ingredients(menu, coffee_type) 
    change = payment - cost
    return change

def ask():
    """Prompts the user to select a coffee type or a special command."""
    valid_choices = ["espresso", "latte", "cappuccino", "report", "off"]

    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input in valid_choices:
            return user_input
        else:
            print("Please enter a valid command.")
            

def coffee_machine_report():
    '''Allows printing of the remaining resources inside the machine'''
    print(f"Water: {full_water} ml")
    print(f"Coffee: {full_coffee} g")
    print(f"Milk: {full_milk} ml")
    print(f"Money: ${money}")
    
coffee_machine(MENU, ask)