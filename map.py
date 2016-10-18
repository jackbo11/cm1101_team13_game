from items import *

room_outside = {
    "name": "Outside",

    "description":
    """You are now staying outside the SU. Where would you like to go?
    You can go south-east to the Dancefloor or north to take taxi to go Talybont.""",

    "exits": {"south-east": "Dancefloor", "north": "Taxi"},
    "time_cost": {"south-east": 3, "north": 2},
    "items": []
}

room_bar1 = {
    "name": "Bar1",

    "description":
    """You are now in bar1. Do you want some drinks?
    A single for £2 and water is free. 
    You can go east to the Dancefloor.""",

    "exits":  {"east": "Dancefloor"},
    "time_cost": {"east": 2},

    "items": [item_single, item_water]
}

room_bar2 = {
    "name": "Bar2",

    "description":
    """You are now in bar2. Do you want some drinks?
    A beer for £3, a double for £5 and water is free. 
    You can go north-east to the Dancefloor or south-east to the Balcony.""",

    "exits": {"north-east": "Dancefloor", "south-east": "Balcony"},
    "time_cost": {"north-east": 7, "south-east": 4},

    "items": [item_beer, item_double, item_water]
}

room_bar3 = {
    "name": "Bar3",

    "description":
    """You are now in bar3. Do you want some drinks?
    A beer for £3, a VK for £3, a single for £2 and water is free. 
    You can go north to the Balcony to keep your mind awake.""",

    "exits": {"north": "Balcony"},
    "time_cost": {"north": 5,},

    "items": [item_beer, item_VK, item_single, item_water]
}

room_toilet = {
    "name": "Toilet",

    "description":
    """You are in the toliet. You can go west to the Dance Floor,""",

    "exits": {"west": "Dancefloor"},
    "time_cost": {"west": 7},
    "items": []
}

room_balcony = {
    "name": "Balcony",

    "description":
    """You are standing in the cool breeze of the wind and feel better.
    You can go north-west to the Bar2, south to the Bar3 or north to the Dancefloor. """,

    "exits": {"north-west": "Bar2", "south": "Bar3", "north": "Dancefloor"},
    "time_cost": {"north-west": 4, "south": 5, "north": 4},
    "items": []
}


room_dancefloor = {
    "name": "Dance Floor",

    "description":
    """You are dancing on the dancefloor with your friends. 
    You feel very hyper and excited after dancing.
    Where would you like to go after dancing? 
    You can go north-west to the outside, west to the Bar1, south-west to the bar2, south to the Balcony, east to the toliet or north to the food. """,

    "exits": {"west": "Bar1", "south": "Balcony", "north-west": "Outside", "north": "Food", "south-west": "Bar2", "east": "Toliet"},
    "time_cost": {"west": 2, "south": 4, "north-west": 3, "north": 4, "south-west": 7, "east": 7},

    "items": []
}

room_food = {
    "name": "Food",

    "description":
    """You smell the yummy food. Would you like to get a burger for £3? You can go south to the Dancefloor or eat a burger.""",

    "exits": {"south": "Dancefloor"},
    "time_cost": {"south": 4},

    "items": [item_burger]
}

room_taly = {
    "name": "Talybont",

    "description":
    """You are in Talybont North having pre drinks.""",

    "exits": {"south": "Taxi"},
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
