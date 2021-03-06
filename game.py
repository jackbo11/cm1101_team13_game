#!/usr/bin/python3

from map import rooms
from items import *
from gameparser import *
import player
import gametime
import ring_of_fire
import sounds
from soundplayer import SoundPlayer
import events
import atm
import sys

player1 = player.Player()
timer = gametime.GameTime()


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_driving_license, item_id])
    'driving license, id card'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_drink, item_wine])
    'money, a drink, a bottle of wine'

    """
    return ", ".join(str(item["name"]) for item in items)


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if room["items"]:
        print("There is {0} here.\n".format(list_of_items(room["items"])))


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(player1.inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if items:
        print("You have {0}.\n".format(list_of_items(items)))


def print_consumables_in_room(room):
    print_consumables(room["consumables"])


def print_consumables(items):
    if items:
        print("You can get {0}.\n".format(list_of_items(items)))


def apply_consumable_effect_by_id(consumable, player, room):
    try:
        consumable_item = [item for item in room["consumables"] if item.get('id') == consumable][0]
        if can_player_afford(player, consumable_item["price"]) == False:
            print("You do not have enough money to get this item!")
        else:
            apply_consumable_effect(consumable_item , player)
    except:
        print("You cannot get a {0} here.".format(consumable))

def apply_consumable_effect(consumable, player):
    if "drink_left_effect" in consumable:
        player.fill_drink(consumable["drink_left_effect"])
    if "happiness_effect" in consumable:
        player.increase_happiness(consumable["happiness_effect"])
    if "drunkenness_effect" in consumable:
        player.increase_drunkenness(consumable["drunkenness_effect"])
    if "price" in consumable:
        player.pay(consumable["price"])


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    #
    # COMPLETE ME!
    #
    print_room_items(room)
    print_consumables_in_room(room)


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    cash_atm_checker(player1)
    print("You can:")
    print("TIME")
    print("STATS")
    print("DRINK")
    if player1.smoker:
        print("SMOKE")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    #
    # COMPLETE ME!
    #
    for room_item in room_items:
        print("TAKE {0} to take {1}.".format(room_item["id"].upper(), room_item["name"]))
    for inv_item in inv_items:
        print("DROP {0} to drop {1}.".format(inv_item["id"].upper(), inv_item["name"]))
    print("The time is now {0}, you have £{1}.".format(timer.time, player1.money))
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def can_player_afford_room(player, room, direction):
    if "money_cost" in room:
        money_to_pay = room["money_cost"][direction]
        if can_player_afford(player, money_to_pay):
            return True
        else:
            return False
    else:
        return True


def can_player_afford(player, amount):
    if amount > player.money:
        return False
    else:
        return True


def add_time_cost(room, direction):
    if "time_cost" in room:
        time_to_add = room["time_cost"][direction]
        timer.add_minutes(time_to_add)


def add_money_cost(room, direction):
    if "money_cost" in room:
        money_to_pay = room["money_cost"][direction]
        player1.pay(money_to_pay)


def verify_player_su(player):
    if (player.age >= 18) and (any(d['id'] == 'id' for d in player.inventory)) and (any(d['id'] == 'drivinglicense' for d in player.inventory)):
        return True
    else:
        return False

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    if is_valid_exit(player1.current_room["exits"], direction) and can_player_afford_room(player1, player1.current_room, direction):

        new_room = move(player1.current_room["exits"], direction)
        # print(new_room)
        if new_room["name"] == "Dance Floor":
            # print(verify_player_su(player1))
            if verify_player_su(player1):
                add_time_cost(player1.current_room, direction)
                add_money_cost(player1.current_room, direction)
                player1.current_room = new_room
            else:
                print("You cannot get in! Are you sure you have your id and driving license? Are you over 18?")
        else:
            add_time_cost(player1.current_room, direction)
            add_money_cost(player1.current_room, direction)
            player1.current_room = new_room
    else:
        print("You cannot go there.")

def execute_get(consumable, player, room):
    apply_consumable_effect_by_id(consumable, player, room)

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    if any(d['id'] == item_id for d in player1.current_room["items"]):
        player1.inventory.extend([item for item in player1.current_room["items"] if item.get('id') == item_id])
        player1.current_room["items"][:] = [item for item in player1.current_room["items"] if item.get('id') != item_id]
    else:
        print("You cannot take that.")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    if any(d['id'] == item_id for d in player1.inventory):
        player1.current_room["items"].extend([item for item in player1.inventory if item.get('id') == item_id])
        player1.inventory[:] = [item for item in player1.inventory if item.get('id') != item_id]
    else:
        print("You cannot drop that.")


def execute_drink(player):
    print(player1.drink())
    print("Your drunkenness is now {0}".format(player.drunkenness))


def execute_smoke(player):
    if player1.smoker:
        if player1.current_room["can_smoke"]:
            print(player1.smoke())
            print("You have {0} cigarettes left.".format(player.cig_left))
        else:
            print("You cannot smoke here.")
    else:
        print("You cannot smoke as you are a non smoker.")


def execute_eval(cmd):
    print(eval(cmd))


def execute_stats():
    print(player1.get_stats())


def execute_clock():
    print("The time is now {0}".format(str(timer.time)))


def execute_sound_test():
    SoundPlayer.play_beep(sounds.song_closer)


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "drink":
        execute_drink(player1)

    elif command[0] == "smoke":
        execute_smoke(player1)

    elif command[0] == "/eval":
        execute_eval(" ".join(command[1:]))

    elif command[0] == "stats":
        execute_stats()

    elif command[0] == "/soundtest":
        execute_sound_test()

    elif command[0] == "time" or command[0] == "clock":
        execute_clock()

    elif command[0] == "get":
        execute_get(command[1], player1, player1.current_room)

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print()
    events.normal_things_happen(player1)
    events.bad_things_happen(player1)
    print()
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def take_inventory_items(items):
    print()
    for room_item in items:
        print("TAKE {0} to take {1}.".format(room_item["id"].upper(), room_item["name"]))
    user_input = input("> ")
    if user_input == "":
        a=True
        while a == True:
            user_input= input("You have to print something!")
            if user_input !="":
                a = False
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def cash_atm_checker(player):
    if player.current_room["name"] == "ATM":
        atm.cash_withdrawal(player)

def take_initial_items():
    while True:
        if player1.current_room["items"]:
            print("There are {0}.\n".format(list_of_items(
                player1.current_room["items"])) + "in your room, you might need some of them in the Student Union")
        command = take_inventory_items(player1.current_room["items"])
        execute_command(command)
        if len(player1.current_room["items"]) > 1:

            for x in range(4):
                if item_id not in player1.inventory:
                    print("Don't you need your Id card to enter the club?")
                    command = take_inventory_items(player1.current_room["items"])
                    execute_command(command)
                elif item_money not in player1.inventory:
                    print("Don't you need some cash to buy some drinks or to get a ride home?")
                    command = take_inventory_items(player1.current_room["items"])
                    execute_command(command)
                elif item_driving_license not in player1.inventory:
                    print("wait, what about your driving license?")
                    command = take_inventory_items(player1.current_room["items"])
                    execute_command(command)
                elif item_keys not in player1.inventory:
                    print("hmmmm, you are going to leave without your keys?")
                    command = take_inventory_items(player1.current_room["items"])
                    execute_command(command)

            else:
                break

        elif len(player1.current_room["items"]) == 1 and item_drink in player1.inventory:
            break


# This is the entry point of our program
def main():
    welcome()
    take_initial_items()
    ring_of_fire.play_ring_of_fire(player1, timer)
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(player1.current_room)
        print_inventory_items(player1.inventory)
        check_player_winning(player1)
        # Show the menu with possible actions and ask the player
        command = menu(player1.current_room["exits"], player1.current_room["items"], player1.inventory)
        # Execute the player's command
        execute_command(command)


def check_player_winning(player):
    if (timer.time_greater_than(3,00,23)) and (player.current_room["name"] == "Talybont"):
        print("Well done, you made it back after a night out! YOU WIN!")
        sys.exit()
    if (timer.time_greater_than(1, 30, 23)) and (player.happiness <=3) and (player.current_room["name"] == "Dance Floor"):
        print("You are not happy enough to stay in the club. GAME OVER!")
        sys.exit()
    elif timer.time_greater_than(3,00,23):
        print("It's 3 AM, the lights are on, the night is over. Can you get home?")
        print("A taxi is waiting outside, it costs: £8.")

    if (timer.time_greater_than(5, 00, 23)) and (player.current_room["name"] != "Talybont"):
        print("It is dawn and you didn't make it home! GAME OVER.")
        sys.exit()


def welcome():
    print("Welcome to SU-rvival by team 13.")
    successful_new_player = False
    while successful_new_player == False:
        try:
            player_name = str(input("What is your name? > "))
            player_age = int(input("What is your age? > "))
            player_gender = str(input("And your gender? > "))
            player_smoke = input("Do you smoke? > ")
            global player1
            player1 = player.Player(player_name, player_gender, player_age, player_smoke)
            successful_new_player = True
        except ValueError:
            print("An invalid value was entered. Please try again.")

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
