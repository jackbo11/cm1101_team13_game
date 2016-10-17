
# Ring of Fire

import string
import random
import gameparser


def play_ring_of_fire(player1, timer):
    # Just some variables
    choose = 0
    confirm = 0
    chance = 0
    x = 0

    # Player's progress
    inv = {"turns": 0, "drunk": 0}


    # Player and NPCs
    players = [str(player1.name), "mia", "sophie", "simon", "juan"]

    # Categorys
    farm_animals = ["duck", "chicken", "hen", "cow", "sheep", "pig", "horse", "donkey", "cat", "dog", "alpaca", "emu", "goat", "goose", "llama", "pigeon", "rabbit", "turkey"]
    alcohols = ["gin", "vodka", "beer", "wine", "red wine", "white wine", "rum", "brandy", "whiskey", "shandy", "cider", "champagne", "sake", "eggnog", "sherry", "port", "amaretto", "martini", "jager", "jagermeister", "tequila", "sambuca", "schnaps", "absinthe"]
    colours = ["pink", "red", "orange", "yellow", "brown", "green", "blue", "indigo", "purple", "violet", "black", "white", "grey"]
    eu_countries = ["russia", "germany", "turkey", "france", "britain", "uk", "england", "scotland", "wales", "northern ireland", "ireland", "italy", "spain", "ukraine", "poland", "romania", "holland", "netherlands", "belgium", "greece", "czech republic", "portugal", "sweden", "hungary", "belarus", "austria", "switzerland", "bulgaria", "serbia", "denmark", "finland", "slovakia", "norway", "croatia", "bosnia", "georgia", "moldova", "lithuania", "albania", "macedonia", "slovenia", "latvia", "kosovo", "estonia", "cyprus", "montenegro", "luxembourg", "malta", "iceland", "andorra"]

    # Rhymes
    fire = ["dire", "dwire", "eir", "gire", "gleyre", "guire", "gyr", "hire", "hyre", "ire", "lyre", "meir", "mire", "myre", "phyre", "quire", "schreyer", "scire", "shire", "skier", "smyre", "spire", "squire", "striar", "swire", "twire", "tyre", "wire", "wyre"]
    ring = ["bing", "bling", "bring", "ching", "cling", "cring", "ding", "djing", "dring", "fling", "fring", "ging", "gring", "gstring", "hing", "ing", "jing", "king", "kling", "kring", "ling", "lyng", "ming", "ning", "ping", "pling", "pring", "qing", "ringe", "schwing", "scringe", "shing", "sing", "singh", "sking", "sling", "sping", "sting", "string", "swing", "swinge", "thing", "thring", "thwing", "ting", "tring", "whinge", "wing", "wring", "xing", "ying", "zing"]
    drink = ["bink", "blink", "brink", "chink", "cinq", "cinque", "clink", "dink", "finck", "fincke", "fink", "finke", "flink", "frink", "hinck", "hink", "inc", "ink", "klinck", "klink", "klinke", "krinke", "linc", "linck", "link", "linke", "lynk", "minc", "mink", "minke", "nsync", "pink", "plink", "princ", "prink", "quinque", "quinque", "rinck", "rink", "rinke", "schinke", "schlink", "scink", "shrink", "sink", "sinque", "skink", "slink", "smink", "spink", "stink", "swink", "sync", "think", "trink", "twink", "vink", "wink", "xlink", "zinc", "zinck", "zink", "zinke"]
    club = ["bub", "bubb", "bubbe", "chubb", "clubb", "cub", "drub", "dub", "grub", "grubb", "hub", "jubb", "nub", "pub", "rub", "schlub", "scrub", "shlub", "shrub", "snub", "strub", "strubbe", "stub", "stubbe", "sub", "tub", "tubb"]



    # Start of game
    print("You start the night by playing ring of fire with your flat mates:")
    print(", ".join(x for x in players))



    # Main loop
    while int(inv["turns"]) < 20: # Decides the maximum number of turns

        # YOUR TURN
        if int(inv["turns"]) % 5 == 0:
            print("\n")
            print("It is your turn. Press any key to pick a card!")
            input("")
            card = random.randrange(1, 14) # picks a random card between 1 and 13
            # A
            if int(card) == 1:
                print("You picked an Ace! Everyone drinks.")
                inv["turns"] = inv["turns"] + 1
                player1.drink()
            # 2
            elif int(card) == 2:
                print("2: You! Pick someone else to drink.")
                choice = input(">>> ")
                choice = gameparser.normalise_string(choice)
                while int(choose) == 0:
                    if choice in players:
                        print(str(choice), "took a drink")
                        choose = 1
                        inv["turns"] = inv["turns"] + 1
                    else:
                        print("Who?")
                        choice = input(">>> ")
            # 3
            elif int(card) == 3:
                print("3: Me! Take a drink.")
                inv["turns"] = inv["turns"] + 1
                player1.drink()
            # 4
            elif int(card) == 4:
                if player1.gender == "Female":
                    print("4: Whores! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
                else:
                    print("4: Whores! You don't have to drink")
                    inv["turns"] = inv["turns"] + 1
            # 5
            elif int(card) == 5:
                choice = input("Do you remember rule 5? ")
                choice = gameparser.normalise_string(choice)
                if str(choice) == "thumb" or str(choice) == "thumbs":
                    print("Well done, you don't have to drink")
                    inv["turns"] = inv["turns"] + 1
                else:
                    print("5: Thumbs! Everyone else places their thumb on the table before you. Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
            # 6
            elif int(card) == 6:
                if player1.gender == "Male":
                    print("4: Dicks! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
                else:
                    print("4: Dicks! You don't have to drink")
                    inv["turns"] = inv["turns"] + 1
            # 7
            elif int(card) == 7:
                choice = input("Do you remember rule 7? ")
                choice = gameparser.normalise_string(choice)
                if str(choice) == "heaven":
                    print("Well done, you don't have to drink")
                    inv["turns"] = inv["turns"] + 1
                else:
                    print("7: Heaven! Everyone else puts their hand in the air before you. Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
            # 8
            elif int(card) == 8:
                print("8: Mate! Pick someone else to drink with.")
                choice = input(">>> ")
                choice = gameparser.normalise_string(choice)
                while int(choose) == 0:
                    if choice in players:
                        print("You and", str(choice), "took a drink")
                        choose = 1
                        inv["turns"] = inv["turns"] + 1
                        player1.drink()
                    else:
                        print("who?")
                        choice = input(">>> ")
            #9
            elif int(card) == 9:
                print("9: Rhyme! What word would you like to choose?")
                print(" A : Fire")
                print(" B : Ring")
                print(" C : Drink")
                print(" D : Club")
                option = input(">>> ")
                option = gameparser.normalise_string(option)
                while confirm == 0:
                    if option == "a" or option == "fire":
                        confirm = 1
                    elif option == "b" or option == "ring":
                        confirm = 2
                    elif option == "c" or option == "drink":
                        confirm = 3
                    elif option == "d" or option == "club":
                        confirm = 4
                    else:
                        confirm = 0
                        print("Answer unclear, which category?")
                        option = input(">>> ")
                if confirm == 1:
                    print("What rhymes with fire?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in fire:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 2:
                    print("What rhymes with ring?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in ring:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 3:
                    print("What rhymes with drink?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in drink:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 4:
                    print("What rhymes with club?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in club:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
            # 10
            elif int(card) == 10:
                print("10: Categories! What category would you like to choose?")
                print(" A : Farm Animals")
                print(" B : Alcoholic Drinks")
                print(" C : Colours")
                print(" D : European Countries")
                option = input(">>> ")
                option = gameparser.normalise_string(option)
                while confirm == 0:
                    if option == "a" or option == "farm" or option == "animals":
                        confirm = 1
                    elif option == "b" or option == "alcohol" or option == "drinks":
                        confirm = 2
                    elif option == "c" or option == "colours":
                        confirm = 3
                    elif option == "d" or option == "europe" or option == "countries":
                        confirm = 4
                    else:
                        confirm = 0
                        print("Answer unclear, which category?")
                        option = input(">>> ")
                if confirm == 1:
                    print("The category is farm animals!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in farm_animals:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 2:
                    print("The category is alcoholic drinks!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in alcohols:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 3:
                    print("The category is colours!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in colours:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 4:
                    print("The category is european countries!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in eu_countries:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
            # J
            elif int(card) == 11:
                print("Jack: Single shot! Take one shot of spirits")
                inv["turns"] = inv["turns"] + 1
                player1.drink()

            # Q
            elif int(card) == 12:
                print("Queen: Double shot! Take 2 shots of spirits")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 2
            # K
            elif int(card) == 13:
                print("Oh no! It's a king! Drink the dirty pint")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 5
            choose = 0
            confirm = 0
            chance = 0
            input("")

        # NPC's TURN
        else:
            print("\n")
            x = int(inv["turns"]) % 5
            print("It is", players[int(x)], "'s turn")
            input("")
            card = random.randrange(1, 14) # picks a random card between 1 and 13
            # A
            if int(card) == 1:
                print(players[int(x)], "picked an Ace! Everyone drinks.")
                inv["turns"] = inv["turns"] + 1
                player1.drink()
            # 2
            elif int(card) == 2:
                choose = random.randrange(0, 5)
                print("2: You!", players[int(x)], "picked", players[int(choose)], "to drink.")
                if int(choose) == 0:
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
                else:
                    inv["turns"] = inv["turns"] + 1
            # 3
            elif int(card) == 3:
                print("3: Me!", players[int(x)], "took a drink.")
                inv["turns"] = inv["turns"] + 1
            # 4
            elif int(card) == 4:
                if player1.gender == "Female":
                    print("4: Whores! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
                else:
                    print("4: Whores! You don't have to drink")
                    inv["turns"] = inv["turns"] + 1
            # 5
            elif int(card) == 5:
                choice = input("Do you remember rule 5? ")
                choice = gameparser.normalise_string(choice)
                if str(choice) == "thumb" or str(choice) == "thumbs":
                    print("Well done, you don't have to drink")
                    inv["turns"] = inv["turns"] + 1
                else:
                    print("5: Thumbs! Everyone else places their thumb on the table before you. Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
            # 6
            elif int(card) == 6:
                if player1.gender == "Male":
                    print("4: Dicks! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
                else:
                    print("4: Dicks! You don't have to drink")
                    inv["turns"] = inv["turns"] + 1
            # 7
            elif int(card) == 7:
                choice = input("Do you remember rule 7? ")
                choice = gameparser.normalise_string(choice)
                if str(choice) == "heaven":
                    print("Well done, you don't have to drink")
                    inv["turns"] = inv["turns"] + 1
                else:
                    print("7: Heaven! Everyone else puts their hand in the air before you. Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
            # 8
            elif int(card) == 8:
                choose = random.randrange(0, 5)
                print("8: Mate!", players[int(x)], "picked", players[int(choose)], "to drink with.")
                if int(choose) == 0:
                    inv["turns"] = inv["turns"] + 1
                    player1.drink()
                else:
                    inv["turns"] = inv["turns"] + 1
            # 9
            elif int(card) == 9:
                print("10: Rhyme!")
                confirm = random.randrange(1, 5)
                if confirm == 1:
                    print(players[int(x)], "chose the word 'fire'!")
                    print("What rhymes with fire?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in fire:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 2:
                    print(players[int(x)], "chose the word 'ring'!")
                    print("What rhymes with ring?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in ring:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 3:
                    print(players[int(x)], "chose the word 'drink'!")
                    print("What rhymes with drink?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in drink:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 4:
                    print(players[int(x)], "chose the word 'club'!")
                    print("What rhymes with club?")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in club:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
            # 10
            elif int(card) == 10:
                print("10: Categories!")
                confirm = random.randrange(1, 5)
                if confirm == 1:
                    print(players[int(x)], "chose the category farm animals!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in farm_animals:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 2:
                    print(players[int(x)], "chose the category alcoholic drinks!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in alcohols:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 3:
                    print(players[int(x)], "chose the category colours!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in colours:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
                elif confirm == 4:
                    print(players[int(x)], "chose the category european countries!")
                    print("Please name one")
                    while chance != 3:
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in eu_countries:
                            print("\n")
                            print("Correct")
                            chance = random.randrange(0, 4)
                            if chance == 3:
                                print("Someone else can't think of an answer. They drink and that round ends")
                                inv["turns"] = inv["turns"] + 1
                            else:
                                print("Everyone else also thinks of an answer, now it is your turn again")
                        else:
                            print("\n")
                            print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            player1.drink()
                            chance = 3
            # J
            elif int(card) == 11:
                print("Jack: Single shot!", players[int(x)], "took one shot of spirits")
                inv["turns"] = inv["turns"] + 1
                player1.drink()

            # Q
            elif int(card) == 12:
                print("Queen: Double shot!", players[int(x)], "took two shots of spirits")
                inv["turns"] = inv["turns"] + 1
                player1.drink(2)
            # K
            elif int(card) == 13:
                print("Oh no! It's a king! Drink the dirty pint")
                inv["turns"] = inv["turns"] + 1
                player1.drink(5)
            choose = 0
            confirm = 0
            chance = 0
            input("")

    print("Player's drunkness got to " + player1.drunkenness)
    input("")
    input("")
