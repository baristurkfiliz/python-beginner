from turtle import clear
from menu import MENU
from resources import resources

def pay(coffee):
    have_to_pay = True
    while have_to_pay:
        cent5 = int(input("Piece of 5 Cent: "))
        cent10 = int(input("Piece of 10 Cent: "))
        cent25 = int(input("Piece of 25 Cent: "))  
        cent50 = int(input("Piece of 50 Cent: "))
        dolar = int(input("Piece of 1 Dolar: "))
        total_money = cent5*0.05 + cent10*0.1 + cent25*0.25 + cent50*0.5 + dolar*1
        if total_money >= MENU[coffee]['cost']:
            remainder = total_money - MENU[coffee]['cost']
            r_dolar = remainder/1
            remainder - r_dolar
            r_cent50 = remainder/0.5
            if r_cent50 >= 1:
                remainder - 0.5
            r_cent25 = remainder/0.25
            if r_cent25 >= 1:
                remainder - 0.25
            r_cent10 = remainder/0.1
            if r_cent10 >= 1:
                remainder - 0.1*r_cent10
            r_cent5 = remainder/0.5
            print(f"Thank you. Your {coffee} is getting ready. You can get your {remainder} dollars change from the machine.")
            have_to_pay = False
        else:
            ballance_error = input("There are not enough money. Take your money back please. If you want to pay again, just write 'pay'. Or press 'enter' to exit.")
            ballance_problem = True
            while ballance_problem:
                if ballance_error == "pay":
                    have_to_pay = True
                    ballance_problem = False
                elif ballance_error == "":
                    print("We are sorry for you don't drink coffee :(")
                    main()
                else:
                    print("Invalid choice.")
            

def check(coffee):
    if MENU[coffee]['ingredients']['water'] <= resources['water']:
        if MENU[coffee]['ingredients']['milk'] <= resources['milk']:
            if MENU[coffee]['ingredients']['coffee'] <= resources['coffee']:
                pay(coffee)
                resources['water'] -= MENU[coffee]['ingredients']['water']
                resources['milk'] -= MENU[coffee]['ingredients']['milk']
                resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
            else:
                print(f"Not enough coffee for {coffee}")
        else:
            print(f"Not enough milk for {coffee}")
    else:
        print(f"Not enough water for {coffee}")
    
def main():
    order = input("What would you like? (espresso/latte/cappuccino):  ")
    if order == "report":
        print(f"Water: {resources['water']}ml".format(resources))
        print(f"Milk: {resources['milk']}ml".format(resources))
        print(f"Coffee: {resources['coffee']}g".format(resources))
    elif order == "latte":
        check(coffee = 'latte')
    elif order == "espresso":
        check(coffee = 'espresso')
    elif order == "cappuccino":
        check(coffee = 'cappuccino')
    elif order == "off":
        exit()
    else:
        print("Unkown command")
    main()
    
    
main()
        