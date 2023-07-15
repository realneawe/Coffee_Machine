MENU = {
    "espresso":
    {
        "ingredients":
        {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":
    {
        "ingredients":
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":
    {
        "ingredients":
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 5000,
    "milk": 2000,
    "coffee": 1000,
}
wallet = 0
remainder_source = [5000, 2000, 1000]

def iron_cash():
    global wallet
    c25 = 0.25
    c50 = 0.50
    d1 = 1.00
    put_d1 = int(input("How many 1 $ will you put in the machine?\n"))
    wallet += (d1 * put_d1)
    put_c50 = int(input("How many 50 cent will you put in the machine?\n"))
    wallet += (c50 * put_c50)
    put_c25 = int(input("How many 25 cent will you put in the machine?\n"))
    wallet += (c25 * put_c25)
    return f"Total money {wallet}$ in machine."

def remainder_espresso():
    global remainder_source
    remainder_source[0] -= int(MENU["espresso"]["ingredients"]["water"])
    remainder_source[2] -= int(MENU["espresso"]["ingredients"]["coffee"])
    return remainder_source

def remainder_latte():
    global remainder_source
    remainder_source[0] -= int(MENU["latte"]["ingredients"]["water"])
    remainder_source[1] -= int(MENU["latte"]["ingredients"]["milk"])
    remainder_source[2] -= int(MENU["latte"]["ingredients"]["coffee"])
    return remainder_source

def remainder_cappuccino():
    global remainder_source
    remainder_source[0] -= int(MENU["cappuccino"]["ingredients"]["water"])
    remainder_source[1] -= int(MENU["cappuccino"]["ingredients"]["milk"])
    remainder_source[2] -= int(MENU["cappuccino"]["ingredients"]["coffee"])
    return remainder_source

# todo: Malzeme tükendiğinde kodu ona göre çıktı verdirip uyarı ile kodu bitirilecek...Versiyon 2'de bunu yapacağım...
end = True
while end:
    end = False
    choose_check = True
    while choose_check:
        choose_check = False
        choose = input("You choose the coffee ('Espresso(e)', 'Latte(l)', 'Cappuccino(c)') in machine; ").lower()

        if choose == "report":
            print(f"Remaining water in machine; {remainder_source[0]}ml\n"
                  f"Remaining milk in machine; {remainder_source[1]}ml\n"
                  f"Remaining coffee in machine; {remainder_source[2]}gr")
            choose_check = True
        else:
            if choose == "espresso" or choose == "e":
                print(f"Your choose is Espresso, this coffe cost is {MENU['espresso']['cost']}$")
                print(iron_cash())
                result_cash = wallet - float(MENU['espresso']['cost'])
                if result_cash == 0:
                    print("Thanks for paying! Enjoy for drink :D")
                    remainder_espresso()
                else:
                    result = result_cash * -1
                    if result > 0:
                        print(f"still not enough money in machine!\nRequired money is {result}$\n"
                              f"All your money has been refunded try again please!")
                        wallet = 0
                        choose_check = True
                    else:
                        change = result * -1
                        print(f"Your change is; {change}$\nThanks for paying! Enjoy for drink. "
                              f"Don't forget to take your change :D")
                        remainder_espresso()
            elif choose == "latte" or choose == "l":
                print(f"Your choose is Espresso, this coffe cost is {MENU['latte']['cost']}$")
                print(iron_cash())
                result_cash = wallet - float(MENU['latte']['cost'])
                if result_cash == 0:
                    print("Thanks for paying! Enjoy for drink :D")
                    remainder_latte()
                else:
                    result = result_cash * -1
                    if result > 0:
                        print(f"still not enough money in machine!\nRequired money is {result}$\n"
                              f"All your money has been refunded try again please!")
                        wallet = 0
                        choose_check = True
                    else:
                        change = result * -1
                        print(f"Your change is; {change}$\nThanks for paying! Enjoy for drink. "
                              f"Don't forget to take your change :D")
                        remainder_latte()
            elif choose == "cappuccino" or choose == "c":
                print(f"Your choose is Espresso, this coffe cost is {MENU['cappuccino']['cost']}$")
                print(iron_cash())
                result_cash = wallet - float(MENU['cappuccino']['cost'])
                if result_cash == 0:
                    print("Thanks for paying! Enjoy for drink :D")
                    remainder_cappuccino()
                else:
                    result = result_cash * -1
                    if result > 0:
                        print(f"still not enough money in machine!\nRequired money is {result}$\n"
                              f"All your money has been refunded try again please!")
                        wallet = 0
                        choose_check = True
                    else:
                        change = result * -1
                        print(f"Your change is; {change}$\nThanks for paying! Enjoy for drink. "
                              f"Don't forget to take your change :D")
                        remainder_cappuccino()
            else:
                print("\nWrong input!\nTry again, your check answer please!\n")
                choose_check = True
    end_choose_check = True
    while end_choose_check:
        end_choose_check = False
        wallet = 0
        end_check = input("\nDo you want another coffee?\nYes(y) or No(n);\n").lower()
        if end_check == "yes" or end_check == "y":
            # print(f"Remaining water in machine; {remainder_source[0]}ml\n"
            #       f"Remaining milk in machine; {remainder_source[1]}ml\n"
            #       f"Remaining coffee in machine; {remainder_source[2]}gr")
            end = True
        elif end_check == "no" or end_check == "n":
            print("Thanks for paying! Enjoy for drink.")
        else:
            print("\nWrong input!\nTry again, check your answer please!\n")
            end_choose_check = True
