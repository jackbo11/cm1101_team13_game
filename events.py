import random
import gameparser
from soundplayer import SoundPlayer
import sounds


def bad_things_happen(player):
    if player.drunkenness >= 9.5:
        r = random.randrange(0, 6)

        if r == 0:
            player.inventory.remove(player.inventory[r])
            print("You lose one of your items of being too drunk.")

        elif r == 1:
            print("You are too drunk, you cannot enter the Student Union.")
            player.increase_happiness(-2)

        elif r == 2:
            print("Oops! You spilt your drink")
            player.increase_drunkenness(-2)
            player.increase_happiness(-2)
            player.drink_left = player.happiness - 1

        elif r == 3:
            print("Oops! You spilt your drink down someone!")
            u = input("They shove you on the shoulder. Do you get in fight or buy them a drink >")
            u = gameparser.normalise_string(u)
            if u == "fight":
                print("You both get a couple of punches and broken up by the bouncer.")
                player.increase_drunkenness(-1)
                player.increase_happiness(-2)
            if u == "drink":
                print("You go to the bar and buy them a drink")
                player.pay(2)
        elif r == 4:
            print("Oops! You spilt someone's drink!")
            u = input("They shove you on the shoulder. Do you get in fight or buy them a drink >")
            u = gameparser.normalise_string(u)
            if u == "fight":
                print("You both get a couple of punches and broken up by the bouncer.")
                player.increase_drunkenness(-1)
                player.increase_happiness(-2)
            if u == "drink":
                print("You go to the bar and buy them a drink")
                player.pay(2)
        elif r == 5:
            print("You are too drunk that you fall down")

    elif player.money == 0:
        player.increase_happiness(-2)
        player.increase_drunkenness(-1)


def normal_things_happen(player):
    if player.current_room["name"] == "Dance Floor":
        r = random.randrange(0, 5)

        if r == 0:
            print("Your favourite song comes on, and you have a great time listening to it.")
            player.increase_happiness(1)
            SoundPlayer.play_beep(sounds.song_closer)

        if r == 1:
            print("You hate this song, and 5 minutes of your life will never get back.")
            player.increase_happiness(-2)

        if r == 2:
            if player.gender == 'Male':
                print("You get chatting to a girl and get her number. Nice Work!")
            else:
                print("You get chatting to a guy and get his number. Nice Work!")

            player.increase_happiness(1)

        if r == 3:
            print("Your friend buys you a drink")
            player.increase_happiness(1)

        if r == 4:
            # Add this a command
            # print("you buy your friend a drink")
            # player.increase_happiness(2)
            # player.pay(2)
            pass
