from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        # print report
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        # check resources sufficient, process coins, check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # make coffee
            coffee_maker.make_coffee(drink)
    else:
        print("Entering wrong!\n")
