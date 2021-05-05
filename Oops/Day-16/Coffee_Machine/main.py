from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

is_on=True



while is_on :
    order=menu.get_items()
    coffee_Name=input (f"What would you like? {order}:")
        
    if(coffee_Name=="Report" or coffee_Name=="report"):
        coffee_maker.report()
        money_machine.report()
    elif(coffee_Name=="off"):
        is_on=False
    else:
        drink=menu.find_drink(coffee_Name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
 