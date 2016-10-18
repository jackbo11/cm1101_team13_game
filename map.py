from items import *

room_outside = {
    "name": "Outside",

    "description":
    """You are now staying outside the SU. Where would you like to go?
    You can go south-east to the Dancefloor, east to get some food or north is take taxi to go home. """,

    "exits": {"south-east": "Dancefloor", "east": "Food", "north": "Taxi"},
    "time_cost": {"south-east": 3, "east": 4, "north": 2},
    "items": []
}

room_bar1 = {
    "name": "Bar1",

    "description":
    """You are now in bar1. Do you want some drinks?
    A single for £2 and water is free. 
    You can go east to the Dancefloor or south to the Bar2.""",

    "exits":  {"east": "Dancefloor", "south": "Bar2"},
    "time_cost": {"east": 2, "south": 4},

    "items": [item_single, item_water]
}

room_bar2 = {
    "name": "Bar2",

    "description":
    """You are now in bar2. Do you want some drinks?
    A beer for £3, a double for £5 and water is free. 
    You can go east to the Balcony or north to the Bar1.""",

    "exits": {"east": "Balcony", "north": "Bar1"},
    "time_cost": {"east": 7, "north": 4},

    "items": [item_beer, item_double, item_water]
}

room_bar3 = {
    "name": "Bar3",

    "description":
    """You are now in bar3. Do you want some drinks?
    A beer for £3, a VK for £3, a single for £2 and water is free. 
    You can go north to the Balcony to keep your mind awake, east to the Toliet or west to the Bar 2.""",

    "exits": {"north": "Balcony", "east": "Toilet", "west": "Bar2"},
    "time_cost": {"north": 5, "east": 7, "west": 7},

    "items": [item_beer, item_VK, item_single, item_water]
}

room_toilet = {
    "name": "Toilet",

    "description":
    """You are in the toliet. You can go west to the Bar3,""",

    "exits": {"west": "Bar3"},
    "time_cost": {"west": 7},
    "items": []
}

room_balcony = {
    "name": "Balcony",

    "description":
    """You are standing in the cool breeze of the wind and feel better.
    You can go east to the toliet, south to the Bar3, 
    west to the Bar 2 or north to the Dancefloor. """,

    "exits": {"east": "Toilet", "south": "Bar3", "west": "Bar2", "north": "Dancefloor"},
    "time_cost": {"east": 7, "south": 5, "west": 7, "north": 4},
    "items": []
}


room_dancefloor = {
    "name": "Dance Floor",

    "description":
    """You are dancing on the dancefloor with your friends. 
    You feel very hyper and excited after dancing.
    Where would you like to go after dancing? 
    You can go west to the Bar1 or south to the Balcony. """,

    "exits": {"west": "Bar1", "south": "Balcony", "north-west": "outside", "north": "food"},
    "time_cost": {"west": 2, "south": 4, "north-west": 3, "north": 4},

    "items": []
}

room_food = {
    "name": "Food",

    "description":
    """You smell the yummy food. Would you like to get a burger for £3?""",

    "exits": {"south": "Dancefloor", "west": "Outside"},
    "time_cost": {"south": 4, "west": 4},

    "items": [item_burger]
}

room_taly = {
    "name": "Talybont",

    "description":
    """You are in Talybont North having pre drinks.""",

    "exits": {"south": "taxi"},
    "time_cost": {"south": 2},

    "items": []
}

room_taxi = {
    "name": "Taxi",

    "description":
    """You are in a taxi. You can go south to the outside of the SU or go north to Talybont.""",

    "exits": {"south": "Outside", "north": "Talybont"},
    "time_cost": {"south": 15, "north": 15},
    "money_cost": {"south": 12, "north": 12},
    "items": []
}

rooms = {
    "Dancefloor": room_dancefloor,
    "Outside": room_outside,
    "Food": room_food,
    "Bar1": room_bar1,
    "Bar2": room_bar2,
    "Bar3": room_bar3,
    "Balcony": room_balcony,
    "Toilet": room_toilet,
    "Talybont": room_taly,
    "Taxi": room_taxi
    
}
