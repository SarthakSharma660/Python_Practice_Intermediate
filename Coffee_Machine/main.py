from data import MENU,resources

milk_amount=resources['milk']
water_amount=resources['water']
coffee_amount=resources['coffee']
money_inn=0
machine_on=True

def report(milk,water,coffee,money):
    """Display the stock available"""
    return (f"Water: {water}ml\n Milk: {milk}ml \nCoffee: {coffee}g \n Money: ${money}")


def calc_money(type):
    global money_inn
    print("Please insert coins.")
    quaters_input=int(input("how many quarters?: "))
    dimes_input= int(input("how many dimes?: "))
    nickels_input= int(input("how many nickles?: "))
    pennies_input=int(input("how many pennies?: "))
    total_money=((quaters_input*0.25)+(dimes_input*0.10)+(nickels_input*0.05)+(pennies_input*0.01))
    if total_money==MENU[type]["cost"]:
        money_inn+=total_money
        return(" Here is $0.0 in change.\n Here is your espresso ☕️. Enjoy!")
    elif total_money>MENU[type]["cost"]:
        money_inn+=total_money
        change=total_money-MENU[type]["cost"]
        money_inn=money_inn-change
        return(f" Here is ${change} in change.\n Here is your espresso ☕️. Enjoy!")
    else:
        return("Sorry that's not enough money. Money refunded.")


def stock_remain(coffee_type):
    """Takes order and claculate money according to it """
    global water_amount, milk_amount, coffee_amount
    if coffee_type==MENU["espresso"]:
        water_amount=water_amount-MENU["espresso"]["ingredients"]["water"]
        coffee_amount=coffee_amount-MENU["espresso"]["ingredients"]["coffee"]
        return water_amount,coffee_amount
    else:
        water_amount=water_amount-MENU[coffee_type]["ingredients"]["water"]
        coffee_amount=coffee_amount-MENU[coffee_type]["ingredients"]["coffee"]
        milk_amount=milk_amount-MENU[coffee_type]["ingredients"]["milk"]
        return water_amount,coffee_amount,milk_amount


def check_stock(coffee) :
    """Take user input to check the stock"""
    global water_amount, milk_amount, coffee_amount
    temp=0
    for key in MENU[coffee]["ingredients"]:
        if water_amount<MENU[coffee]["ingredients"][key] :
            temp=1
            return(f"Sorry there is not enough {key}.")
    if temp==0:
        return True

while machine_on:   
    order=input(" What would you like? (espresso/latte/cappuccino) : ").lower()

    if order=="report":
        print(report(milk=milk_amount,water=water_amount,coffee=coffee_amount,money=money_inn))
    elif order=="off":
      machine_on==False
    else:
        is_stock_there=check_stock(coffee=order)
        if check_stock(order):
            print(calc_money(type=order))
        else:
            print(is_stock_there)
        water_amount,coffee_amount,milk_amount=stock_remain(order)
