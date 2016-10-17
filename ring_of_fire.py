
# Ring of Fire

import string
import random

#Formatting
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct

def remove_spaces(text):
    stripped =  text.strip()
    return stripped

def normalise_input(user_input):
    no_punct = remove_punct(user_input).lower()
    normalised = remove_spaces(no_punct)
    return normalised



# Just some variables
gen = 0
choose = 0
confirm = 0
chance = 0
x = 0


# Name input
print("What is your name?")
name = input(">>> ")
name = normalise_input(name)
print("\n")


# Gender input
print("What is your gender? (m/f)")
gender = input(">>> ")
gender = normalise_input(gender)
while int(gen) == 0:
    if str(gender) == "m" or str(gender) == "male":
        gen = 1
    elif str(gender) == "f" or str(gender) == "female":
        gen = 2
    else:
        print("What?")
        gender = input(">>> ")
    print("\n")


# Player's progress
inv = {"turns": 0, "drunk": 0}


# Player and NPCs
players = [str(name), "mia", "sophie", "simon", "juan"]

#Categorys
farm_animals = ["duck", "chicken", "hen", "cow", "sheep", "pig", "horse", "donkey", "cat", "dog", "alpaca", "emu", "goat", "goose", "llama", "pigeon", "rabbit", "turkey"]
alcohols = ["gin", "vodka", "beer", "wine", "red wine", "white wine", "rum", "brandy", "whiskey", "shandy", "cider", "champagne", "sake", "eggnog", "sherry", "port", "amaretto", "martini", "jager", "jagermeister", "tequila", "sambuca", "schnaps", "absinthe"]
colours = ["pink", "red", "orange", "yellow", "brown", "green", "blue", "indigo", "purple", "violet", "black", "white", "grey"]
eu_countries = ["russia", "germany", "turkey", "france", "britain", "uk", "england", "scotland", "wales", "northern ireland", "ireland", "italy", "spain", "ukraine", "poland", "romania", "holland", "netherlands", "belgium", "greece", "czech republic", "portugal", "sweden", "hungary", "belarus", "austria", "switzerland", "bulgaria", "serbia", "denmark", "finland", "slovakia", "norway", "croatia", "bosnia", "georgia", "moldova", "lithuania", "albania", "macedonia", "slovenia", "latvia", "kosovo", "estonia", "cyprus", "montenegro", "luxembourg", "malta", "iceland", "andorra"]





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
        card = random.randrange(1, 11) # picks a random card between 1 and 13
        # A
        if int(card) == 1:
            print("You picked an Ace! Everyone drinks.")
            inv["turns"] = inv["turns"] + 1
            inv["drunk"] = inv["drunk"] + 1
        # 2
        elif int(card) == 2:
            print("2: You! Pick someone else to drink.")
            choice = input(">>> ")
            choice = normalise_input(choice)
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
            inv["drunk"] = inv["drunk"] + 1
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
            choice = normalise_input(choice)
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
            choice = normalise_input(choice)
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
            choice = normalise_input(choice)
            while int(choose) == 0:
                if choice in players:
                    print("You and", str(choice), "took a drink")
                    choose = 1
                    inv["turns"] = inv["turns"] + 1
                    inv["drunk"] = inv["drunk"] + 1
                else:
                    print("who?")
                    choice = input(">>> ")
        # 10
        elif int(card) == 10:
            print("10: Categories!")
            confirm = random.randrange(1, 5)
            if confirm == 1:
                print("The category is farm animals!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
            elif confirm == 2:
                print("The category is alcoholic drinks!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
            elif confirm == 3:
                print("The category is colours!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
            elif confirm == 4:
                print("The category is european countries!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
        # K
        elif int(card) == 9:
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
        card = random.randrange(1, 11) # picks a random card between 1 and 13
        # A
        if int(card) == 1:
            print(players[int(x)], "picked an Ace! Everyone drinks.")
            inv["turns"] = inv["turns"] + 1
            inv["drunk"] = inv["drunk"] + 1
        # 2
        elif int(card) == 2:
            choose = random.randrange(0, 5)
            print("2: You!", players[int(x)], "picked", players[int(choose)], "to drink.")
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
            choice = normalise_input(choice)
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
            choice = normalise_input(choice)
            if str(choice) == "heaven":
                print("Well done, you don't have to drink")
                inv["turns"] = inv["turns"] + 1
            else:
                print("7: Heaven! Everyone else puts their hand in the air before you. Take a drink")
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 1
        # 8
        elif int(card) == 8:
            choose = random.randrange(0, 5)
            print("8: Mate!", players[int(x)], "picked", players[int(choose)], "to drink with.")
            if int(choose) == 0:
                inv["turns"] = inv["turns"] + 1
                inv["drunk"] = inv["drunk"] + 1
            else:
                inv["turns"] = inv["turns"] + 1
        # 10
        elif int(card) == 10:
            print("10: Categories!")
            confirm = random.randrange(1, 5)
            if confirm == 1:
                print("The category is farm animals!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
            elif confirm == 2:
                print("The category is alcoholic drinks!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
            elif confirm == 3:
                print("The category is colours!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3
            elif confirm == 4:
                print("The category is european countries!")
                print("Please name one")
                while chance != 3:
                    choice = input(">>> ")
                    choice = normalise_input(choice)
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
                        inv["drunk"] = inv["drunk"] + 1
                        chance = 3

        # K
        elif int(card) == 9:
            print("Oh no! It's a king!", players[int(x)], "drank the dirty pint")
            inv["turns"] = inv["turns"] + 1
            inv["drunk"] = inv["drunk"] + 5
        choose = 0
        confirm = 0
        input("")
