import string
import random
import gameparser


def play_ring_of_fire(player1, timer):

    # Just some variables
    choose = 0
    confirm = 0
    chance = 0
    x = 0
    npc1 = ""
    npc2 = ""
    npc3 = ""
    npc4 = ""
    wordlist = []
    
    # Converts gender to integer
    if player1.gender == "Male":
        gen = 1
    elif player1.gender == "Female":
        gen = 2

    # Player's progress
    inv = {"turns": 0, "drunk": 0}

    # Categories
    farm_animals = ["duck", "chicken", "hen", "cow", "sheep", "pig", "horse", "donkey", "cat", "dog", "alpaca", "emu", "goat", "goose", "llama", "pigeon", "rabbit", "turkey"]
    alcohols = ["gin", "vodka", "beer", "wine", "red wine", "white wine", "rum", "brandy", "whiskey", "shandy", "cider", "champagne", "sake", "eggnog", "sherry", "port", "amaretto", "martini", "jager", "jagermeister", "tequila", "sambuca", "schnaps", "absinthe"]
    colours = ["pink", "red", "orange", "yellow", "brown", "green", "blue", "indigo", "purple", "violet", "black", "white", "grey"]
    eu_countries = ["russia", "germany", "turkey", "france", "britain", "uk", "england", "scotland", "wales", "northern ireland", "ireland", "italy", "spain", "ukraine", "poland", "romania", "holland", "netherlands", "belgium", "greece", "czech republic", "portugal", "sweden", "hungary", "belarus", "austria", "switzerland", "bulgaria", "serbia", "denmark", "finland", "slovakia", "norway", "croatia", "bosnia", "georgia", "moldova", "lithuania", "albania", "macedonia", "slovenia", "latvia", "kosovo", "estonia", "cyprus", "montenegro", "luxembourg", "malta", "iceland", "andorra"]

    # GAME START
    print("You start the night in your flat with your flat mates, what were their names again?")
    while choose == 0:
        npc1 = input("Flat mate 1: ")
        npc1 = gameparser.normalise_string(npc1)
        if npc1 == "":
            "Not a valid name"
            npc1 = input("Flat mate 1: ")
            choose = 0
        else:
            choose = 1
    choose = 0
    while choose == 0:
        npc2 = input("Flat mate 2: ")
        npc2 = gameparser.normalise_string(npc2)
        if npc2 == "":
            "Not a valid name"
            npc2 = input("Flat mate 2: ")
            choose = 0
        else:
            choose = 1
    choose = 0
    while choose == 0:
        npc3 = input("Flat mate 3: ")
        npc3 = gameparser.normalise_string(npc3)
        if npc3 == "":
            "Not a valid name"
            npc3 = input("Flat mate 3: ")
            choose = 0
        else:
            choose = 1
    choose = 0
    while choose == 0:
        npc4 = input("Flat mate 4: ")
        npc4 = gameparser.normalise_string(npc4)
        if npc4 == "":
            "Not a valid name"
            npc4 = input("Flat mate 4: ")
            choose = 0
        else:
            choose = 1
    choose = 0
    print("\n")

    # Player and NPCs
    players = [str(player1.name), str(npc1), str(npc2), str(npc3), str(npc4)]

    # Describing the game
    print(", ".join(x for x in players))
    print("You start the night by playing the drinking game RING OF FIRE")
    input("")
    print("Each card has a rule, and those rules are...")
    print("\n")
    print(" Ace   : Everybody drinks")
    print(" 2     : You! Pick someone else to drink")
    print(" 3     : Me! You drink")
    print(" 4     : Whores! Girls drink")
    print(" 5     : Thumbs! Last one to put their thumb on the table drinks")
    print(" 6     : Dicks! Boys drink")
    print(" 7     : Heaven! Last one to put their hand in the air drinks")
    print(" 8     : Mate! Pick someone and you both have to drink")
    print(" 9     : Rhyme! Pick a word and everyone has to rhyme with it")
    print(" 10    : Categories! Pick a category of items and everyone has to say one")
    print(" Jack  : Single! Take a single shot")
    print(" Queen : Double! Take a double shot")
    print(" King  : Dirty pint! A mix of everyone else's drink in one cup")
        
    # MAIN LOOP
    # YOUR TURN
    while inv["turns"] < 21:
        timer.add_minutes(4)
        if int(inv["turns"]) % 5 == 0:      # player's turn every 5 turns
            print("\n")
            print("It is your turn. Press any key to pick a card!")
            input("")
            card = random.randrange(1, 14)      # picks a random card between 1 and 13
            # A
            if int(card) == 1:
                print("You picked an Ace! Everyone drinks.")
                inv["turns"] = inv["turns"] + 1     # adds 1 to no. of turns
                inv["drunk"] = inv["drunk"] + 1     # adds 1 to drunkness
            # 2
            elif int(card) == 2:
                print("2: You! Pick someone else to drink.")
                choice = input(">>> ")
                choice = gameparser.normalise_string(choice)
                while int(choose) == 0:                 # loops till a valid NPC has been chosen
                    if choice in players and players[0] != choice:
                        print(str(choice), "took a drink")
                        choose = 1                      # breaks loop
                        inv["turns"] = inv["turns"] + 1
                        inv["drunk"] = inv["drunk"] + 1
                    elif choice in players and players[0] == choice:
                        print("You can't pick yourself!")
                        choice = input(">>> ")
                        choose = 0
                    elif not (choice in players) and players[0] == choice:  # yes I realise this line of code is retarded, but it shows I can use 'not'
                        print("You can't pick yourself!")
                        choice = input(">>> ")
                        choose = 0
                    else:
                        print("who?")
                        choice = input(">>> ")
            # 3
            elif int(card) == 3:
                print("3: Me! Take a drink.")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 1
            # 4
            elif int(card) == 4:
                if int(gen) == 2:       # if gender is female
                    print("4: Whores! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    inv["drunk"] = inv["drunk"] + 1
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
                    inv["drunk"] = inv["drunk"] + 1
            # 6
            elif int(card) == 6:
                if int(gen) == 1:                       #if gender is male
                    print("4: Dicks! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    inv["drunk"] = inv["drunk"] + 1
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
                    inv["drunk"] = inv["drunk"] + 1
            # 8
            elif int(card) == 8:
                print("8: Mate! Pick someone else to drink with.")
                choice = input(">>> ")
                choice = gameparser.normalise_string(choice)
                while int(choose) == 0:                 # loops till a valid NPC has been chosen
                    if choice in players and players[0] != choice:
                        print("You and", str(choice), "took a drink")
                        choose = 1                      # breaks loop
                        inv["turns"] = inv["turns"] + 1
                        inv["drunk"] = inv["drunk"] + 1
                    elif choice in players and players[0] == choice:
                        print("You can't pick yourself!")
                        choice = input(">>> ")
                        choose = 0
                    elif not (choice in players) and players[0] == choice:  # yes I realise this line of code is retarded, but it shows I can use 'not'
                        print("You can't pick yourself!")
                        choice = input(">>> ")
                        choose = 0
                    else:
                        print("who?")
                        choice = input(">>> ")
            #9
            elif int(card) == 9:
                print("9: Rhyme! What word would you like to choose?")
                print(" A : Ring")
                print(" B : Bell")
                print(" C : Mend")
                option = input(">>> ")
                option = gameparser.normalise_string(option)
                while confirm == 0:                     # loops until valid choice is made
                    if option == "a" or option == "ring":
                        confirm = 1
                    elif option == "b" or option == "bell":
                        confirm = 2
                    elif option == "c" or option == "mend":
                        confirm = 3
                    else:
                        confirm = 0
                        print("Answer unclear, which word?")
                        option = input(">>> ")            
                if confirm == 1:
                    print("What rhymes with ring?")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            x = str(choice[-3:])        # last 3 letters
                            if str(x) == "ing":         # last 3 letters must be 'ing'
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 2:
                    print("What rhymes with bell?")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            x = str(choice[-3:])        # last 3 letters
                            if str(x) == "ell":         # last 3 letters must be 'ell'
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 3:
                    print("What rhymes with mend?")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            x = str(choice[-3:])        # last 3 letters
                            if str(x) == "end":         # last 3 letters must be 'end'
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
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
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in farm_animals:  # checks if choice is in the list of valid answers
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 2:
                    print("The category is alcoholic drinks!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in alcohols:      # checks if choice is in the list of valid answers
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 3:
                    print("The category is colours!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in colours:       # checks if choice is in the list of valid answers
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 4:
                    print("The category is european countries!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in eu_countries:  # checks if choice is in the list of valid answers
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
            # J
            elif int(card) == 11:
                print("Jack: Single shot! Take one shot of vodka")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 1

            # Q
            elif int(card) == 12:
                print("Queen: Double shot! Take 2 shots of vodka")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 2         # double, so add 2 to drunkness
            # K
            elif int(card) == 13:
                print("Oh no! It's a king! Drink the dirty pint")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 5         # dirty pint, so add 5 to drunkness

            # RESET VARIABLES
            choose = 0
            confirm = 0
            chance = 0
            x = 0
            wordlist = []
            input("")

        # NPC's TURN
        else:
            print("\n")
            x = int(inv["turns"]) % 5
            print("It is", players[int(x)], "'s turn")
            input("")
            card = random.randrange(1, 14)              # picks a random card between 1 and 13
            # A
            if int(card) == 1:
                print(players[int(x)], "picked an Ace! Everyone drinks.")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 1
            # 2
            elif int(card) == 2:
                choose = random.randrange(0, 5)         # picks a random player
                while chance == 0:
                    if players[int(x)] == players[int(choose)]:           # stops NPCs picking themselves
                        choose = random.randrange(0, 5)
                        chance = 0
                    else:
                        print("2: You!", players[int(x)], "picked", players[int(choose)], "to drink.")
                        chance = 1
                        if int(choose) == 0:
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                        else:
                            inv["turns"] = inv["turns"] + 1
            # 3
            elif int(card) == 3:
                print("3: Me!", players[int(x)], "took a drink.")
                inv["turns"] = inv["turns"] + 1
            # 4
            elif int(card) == 4:
                if int(gen) == 2:
                    print("4: Whores! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    inv["drunk"] = inv["drunk"] + 1
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
                    inv["drunk"] = inv["drunk"] + 1
            # 6
            elif int(card) == 6:
                if int(gen) == 1:
                    print("4: Dicks! Take a drink")
                    inv["turns"] = inv["turns"] + 1
                    inv["drunk"] = inv["drunk"] + 1
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
                    inv["drunk"] = inv["drunk"] + 1
            # 8
            elif int(card) == 8:
                choose = random.randrange(0, 5)         # picks a random player
                while chance == 0:
                    if players[int(x)] == players[int(choose)]:
                        choose = random.randrange(0, 5)
                        chance = 0
                    else:
                        print("8: Mate!", players[int(x)], "picked", players[int(choose)], "to drink with.")
                        chance = 1
                        if int(choose) == 0:
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                        else:
                            inv["turns"] = inv["turns"] + 1
            #9
            elif int(card) == 9:
                print("9: Rhyme!")
                confirm = random.randrange(1, 4)        # chooses a random words to rhyme with          
                if confirm == 1:
                    print("What rhymes with ring?")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            x = str(choice[-3:])
                            if str(x) == "ing":
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 2:
                    print("What rhymes with bell?")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            x = str(choice[-3:])
                            if str(x) == "ell":
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 3:
                    print("What rhymes with mend?")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            x = str(choice[-3:])
                            if str(x) == "end":
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
            # 10
            elif int(card) == 10:
                print("10: Categories!")
                confirm = random.randrange(1, 5)        # chooses a random category
                if confirm == 1:
                    print(players[int(x)], "chose the category farm animals!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in farm_animals:
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 2:
                    print(players[int(x)], "chose the category alcoholic drinks!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in alcohols:
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 3:
                    print(players[int(x)], "chose the category colours!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in colours:
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
                elif confirm == 4:
                    print(players[int(x)], "chose the category european countries!")
                    print("Please name one")
                    while chance != 3:                  # chance of an NPC losing the round
                        choice = input(">>> ")
                        choice = gameparser.normalise_string(choice)
                        if choice in wordlist:          # stops the player repeating answers
                            print("\n")
                            print("You have already said", str(choice), ". You take a drink")
                            inv["turns"] = inv["turns"] + 1
                            inv["drunk"] = inv["drunk"] + 1
                            chance = 3
                        else:
                            wordlist.append(choice)     # adds choice to list of answers so it can't be repeated
                            if choice in eu_countries:
                                print("\n")
                                print("Correct")
                                chance = random.randrange(0, 4)     # 1 in 4 chance of an NPC getting  a wrong answer
                                if chance == 3:
                                    print("Someone else can't think of an answer. They drink and that round ends")
                                    inv["turns"] = inv["turns"] + 1
                                else:
                                    print("Everyone else also thinks of an answer, now it is your turn again")
                            else:
                                print("\n")
                                print(str(choice), "doesn't seem to be a valid answer. You take a drink")
                                inv["turns"] = inv["turns"] + 1
                                inv["drunk"] = inv["drunk"] + 1
                                chance = 3
            # J
            elif int(card) == 11:
                print("Jack: Single shot!", players[int(x)], "took one shot of spirits")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 1

            # Q
            elif int(card) == 12:
                print("Queen: Double shot!", players[int(x)], "took two shots of spirits")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 2
            # K
            elif int(card) == 13:
                print("Oh no! It's a king! Drink the dirty pint")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 5

            # RESET VARIABLES
            choose = 0
            confirm = 0
            chance = 0
            x = 0
            wordlist = []
            input("")

    player1.drunkenness = int(inv["drunk"]) / 4
    input("")
    input("")
