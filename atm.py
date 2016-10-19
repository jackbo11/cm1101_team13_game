
def cash_withdrawal(player1):
    if player1.current_room["name"] == "ATM":
        print("You are now using the ATM:")
        p = input("Enter your passcode, please:")
        if len(p) != 4:

            b = True
            while b == True:
                print("Your passcode should be 4 digits")
                p = input("Enter your passcode, please:")
                if p.isdigit() == True:
                    if len(p) == 4:
                        b = False

       # print(player1.drunkenness)
        if player1.drunkenness >= 7:
            print("Sorry, you are too drunk to remember your passcode")
        else:
            print("Your account balance is: ", player1.bank_money)
            if player1.bank_money >= 5 and player1.bank_money < 10:
                print("Enter the amount of money you want to take out. This machine only accepts the doubles of 5 ")
                i = int(input(">"))
                if i > player1.bank_money or i % 5 != 0:
                    a = True
                    while a == True:
                        ii = int(input("Sorry, the amount entered is whether not a multiplication of 5 or not correct"))
                        print("")
                        if ii <= player1.bank_money and ii % 5 == 0:
                            a = False
                            print("Your transaction is completed, Thank you.")
                            player1.withdraw_from_bank(ii)
                            print("Your new account balance is: ", player1.bank_money)

                else:
                    print("Your transaction is completed, Thank you.")
                    player1.withdraw_from_bank(i)
                    print("Your new account balance is: ", player1.bank_money)

            if player1.bank_money >= 10 and player1.bank_money < 15:
                print("Enter the amount of money you want to take out. This machine only accepts the doubles of 5 ")
                i = int(input(">"))
                if i > player1.bank_money or i % 5 != 0:
                    a = True
                    while a == True:
                        ii = int(input("Sorry, the amount entered is whether not a multiplication of 5 or not correct"))
                        print("")
                        if ii <= player1.bank_money and ii % 5 == 0:
                            a = False
                            print("Your transaction is completed, Thank you.")
                            player1.withdraw_from_bank(ii)
                            print("Your new account balance is: ", player1.bank_money)

                else:
                    print("Your transaction is completed, Thank you.")
                    player1.withdraw_from_bank(i)
                    print("Your new account balance is: ", player1.bank_money)

            if player1.bank_money >= 15 and player1.bank_money <= 20:
                print("Enter the amount of money you want to take out. This machine only accepts the doubles of 5 ")
                i = int(input(">"))
                if i > player1.bank_money or i % 5 != 0:
                    a = True
                    while a == True:
                        ii = int(input("Sorry, the amount entered is whether not a multiplication of 5 or not correct"))
                        print("")
                        if ii <= player1.bank_money and ii % 5 == 0:
                            a = False
                            print("Your transaction is completed, Thank you.")
                            player1.withdraw_from_bank(ii)
                            print("Your new account balance is: ", player1.bank_money)
                else:
                    print("Your transaction is completed, Thank you.")
                    player1.withdraw_from_bank(i)
                    print("Your new account balance is: ", player1.bank_money)

            if player1.bank_money > 20:
                print("Enter the amount of money you want to take out. This machine only accepts the doubles of 5 ")

                i = int(input(">"))
                if i > player1.bank_money or i % 5 != 0:
                    a = True
                    while a == True:
                        ii = int(input("Sorry, the amount entered is whether not a multiplication of 5 or not correct"))
                        print("")
                        if i <= player1.bank_money and ii % 5 == 0:
                            a = False
                            print("Your transaction is completed, Thank you.")
                            player1.withdraw_from_bank(ii)
                            print("Your new account balance is: ", player1.bank_money)
                else:
                    print("Your transaction is completed, Thank you.")
                    player1.withdraw_from_bank(i)
                    print("Your new account balance is: ", player1.bank_money)

