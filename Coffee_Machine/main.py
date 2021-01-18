from data import MENU,resources

milk_amount=resources['milk']
water_amount=resources['water']
coffee_amount=resources['coffee']
money_inn=0
machine_on=True
milk_to_use=water_to_use=coffee_to_use=0
coffee_to_dispach=True

def resources_to_use(type):
    """Take the order form user and return resources to be used"""
    milk=water=coffee=0
    for key in MENU[type]["ingredients"]:
        if key=="milk" :
            milk=MENU[type]["ingredients"][key]
        elif key=="water":
            water=MENU[type]["ingredients"][key]
        else:
            coffee=MENU[type]["ingredients"][key]
    return milk ,water, coffee



def stock_remain(milk,water,coffee,money):
    """Tell the user how much resources are left"""
    global milk_amount,coffee_amount,water_amount,money_inn
    money=money_inn
    milk_amount=milk_amount-milk
    water_amount=water_amount-water
    coffee_amount=coffee_amount-coffee
    return (f"Water: {water}ml\n Milk: {milk}ml \nCoffee: {coffee}g \n Money: ${money}")

def stock_check(milk,water,coffee):
    """check the stock"""
    global coffee_to_dispach
    if milk>milk_amount:
        coffee_to_dispach=False
        return("Sorry there is not enough milk.")
    elif water>water_amount:
        coffee_to_dispach=False
        return("Sorry there is not enough water.")
    elif coffee>coffee_amount:
        coffee_to_dispach=False
        return("Sorry there is not enough coffee.")
    else:
        coffee_to_dispach=True
        return 


def input_money():
    global money_inn
    print("Please insert coins.")
    quaters_input=int(input("how many quarters?: "))
    dimes_input= int(input("how many dimes?: "))
    nickels_input= int(input("how many nickles?: "))
    pennies_input=int(input("how many pennies?: "))
    total_money=((quaters_input*0.25)+(dimes_input*0.10)+(nickels_input*0.05)+(pennies_input*0.01))
    money_inn=total_money
    return total_money


def change_calc(money,type):
    global money_inn,coffee_to_dispach
    change=0.0
    if money>MENU[type]["cost"] or money==MENU[type]["cost"]:
        change=money-MENU[type]["cost"]
        money_inn-=change
        return(f" Here is ${change} in change.\n Here is your espresso ☕️. Enjoy!")
    else:
        coffee_to_dispach=False
        return("Sorry that's not enough money. Money refunded.")  

while machine_on:
    order=input(" What would you like? (espresso/latte/cappuccino) : ").lower()
    if order=="report":
        print(stock_remain(milk=milk_to_use,water=water_to_use,coffee=coffee_to_use,money=money_inn))
    else:
        milk_to_use,water_to_use,coffee_to_use=resources_to_use(order)

    print(stock_check(milk=milk_to_use,water=water_to_use,coffee=coffee_to_use))
    if coffee_to_dispach:
        if order=="off":
            machine_on=False
        else:
            if coffee_to_dispach:
                money_paid=input_money()
                print(change_calc(money=money_paid,type=order))
                stock_remain(milk=milk_to_use,water=water_to_use,coffee=coffee_to_use,money=money_inn)
        
            
