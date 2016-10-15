
# Ring of Fire


import random


def play_ring_of_fire(player, timer):
    choose = 0
    #print("What is your name?")
    #name = input(">>> ")
    print("\n")
    #TEST LINE
    print("Your name is: {0}, you are {1}.".format(str(player.name), str(player.gender)))
    #print("What is your gender? (m/f)")
    #gender = input(">>> ")
    #while int(gen) == 0:
    #    if str(gender) == "m":
    #        gen = 1
    #    elif str(gender) == "f":
    #        gen = 2
    #    else:
    #        print("What?")
    #        gender = input(">>> ")
    #    print("\n")

    inv = {"turns": 0, "drunk": 0}

    players = {str(player.name), "Mia", "Sophie", "Simon", "Juan"}

    def is_player_valid(players, choice):
        if choice in players:
            return True
        else:
            return False


    print("You start the night by playing ring of fire with your flat mates:")
    print(*players)
    print("\n")






    while int(inv["turns"]) < 20:
        # if int(inv["turns"]) % 5 == 0:
        # ^^ commented as I haven't done the code for other players yet
            print("It is your turn. Press any key to pick a card!")
            input("")
            card = random.randrange(1, 13)
            timer.add_minutes(2)
            # card = 2
            #^^ uncomment and change value to test different card values
            # A (works)
            if int(card) == 1:
                print("You picked an Ace! Everyone drinks.")
                inv["turns"] = inv["turns"] + 1
                player.drink()
            # 2 (broken)
            elif int(card) == 2:
                print("2: You! Pick someone else to drink.")
                choice = input(">>> ")
                for choice in players:
                    while int(choose) == 0:
                        if is_player_valid(players, choice):
                            print(str(choice), "took a drink")
                            choose = 1
                            inv["turns"] = inv["turns"] + 1
                        else:
                            print("Who?")
                            choice = input(">>> ")
            # 3 (works)
            elif int(card) == 3:
                print("3: Me! Take a drink.")
                inv["turns"] = inv["turns"] + 1
                player.drink()
            # 4 (works)
            elif int(card) == 4:
                if player.gender == "Female":
                    print("4: Whores! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player.drink()
                else:
                    print("4: Whores! You don't have to drink")
                    inv["turns"] = inv["turns"] + 1
            # 5 (works)
            elif int(card) == 5:
                choose = input("Do you remember rule 5? ")
                if str(choose) == "thumb":
                    print("Well done, you don't have to drink")
                    inv["turns"] = inv["turns"] + 1
                else:
                    print("5: Thumbs! Everyone else places their thumb on the table before you. Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player.drink()
            # 6 (works)
            elif int(card) == 6:
                if player.gender == "Male":
                    print("4: Dicks! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player.drink()
                else:
                    print("4: Dicks! You don't have to drink")
                    inv["turns"] = inv["turns"] + 1
            # 7 (works)
            elif int(card) == 7:
                choose = input("Do you remember rule 7? ")
                if str(choose) == "heaven":
                    print("Well done, you don't have to drink")
                    inv["turns"] = inv["turns"] + 1
                else:
                    print("7: Heaven! Everyone else puts their hand in the air before you. Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player.drink()
            # 8 (broken)
            elif int(card) == 8:
                choice = input("8: Mate! Pick someone else to drink with.")
                #for value in players.items():
                #    while int(choose) == 0:
                #        if str(choice) == value:
                #            print(value, "took a drink")
                #            choose = 1
                #            inv["turns"] = inv["turns"] + 1
                #            player.drink()
                #        else:
                #            print("who?")
            # 9 (uncompleted)
            elif int(card) == 9:
                print("")
            # 10 (uncompleted)
            elif int(card) == 10:
                print("")
            # J (uncompleted)
            elif int(card) == 11:
                print("")
            # Q (uncompleted)
            elif int(card) == 12:
                print("")
            # K (works)
            elif int(card) == 13:
                print("Oh no! It's a king! Drink the dirty pint")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 5
            choose = 0
