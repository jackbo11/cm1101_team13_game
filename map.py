from items import *
import consumables

room_outside = {
    "name": "Outside",

    "description":
    """You are now staying outside the SU. Where would you like to go?
    You can go southeast to the Dancefloor or north to take taxi to go Talybont.""",

    "exits": {"southeast": "Dancefloor", "north": "Taxi"},
    "time_cost": {"southeast": 3, "north": 2},
    "items": [],
    "consumables": []
}

room_bar1 = {
    "name": "Bar1",

    "description":
    """You are now in bar1. Do you want some drinks?
    A single for £2 and water is free. 
    You can go east to the Dancefloor.""",

    "exits":  {"east": "Dancefloor"},
    "time_cost": {"east": 2},

    "items": [],
    "consumables": [consumables.drink_beer, consumables.drink_single, consumables.drink_water]
}

room_bar2 = {
    "name": "Bar2",

    "description":
    """You are now in bar2. Do you want some drinks?
    A beer for £3, a double for £5 and water is free. 
    You can go northeast to the Dancefloor or southeast to the Balcony.""",

    "exits": {"northeast": "Dancefloor", "southeast": "Balcony"},
    "time_cost": {"northeast": 7, "southeast": 4},

    "items": [],
    "consumables": [consumables.drink_VK, consumables.drink_single, consumables.drink_double, consumables.drink_water]
}

room_bar3 = {
    "name": "Bar3",

    "description":
    """You are now in bar3. Do you want some drinks?
    A beer for £3, a VK for £3, a single for £2 and water is free. 
    You can go north to the Balcony to keep your mind awake.""",

    "exits": {"north": "Balcony"},
    "time_cost": {"north": 5,},

    "items": [],
    "consumables": [consumables.drink_water, consumables.drink_VK, consumables.drink_beer]
}

room_toilet = {
    "name": "Toilet",

    "description":
    """You are in the toliet. You can go west to the Dance Floor,""",

    "exits": {"west": "Dancefloor"},
    "time_cost": {"west": 7},
    "items": [],
    "consumables": []
}

room_balcony = {
    "name": "Balcony",

    "description":
    """You are standing in the cool breeze of the wind and feel better.
    You can go northwest to the Bar2, south to the Bar3 or north to the Dancefloor. """,

    "exits": {"northwest": "Bar2", "south": "Bar3", "north": "Dancefloor"},
    "time_cost": {"northwest": 4, "south": 5, "north": 4},
    "items": [],
    "consumables": []
}


room_dancefloor = {
    "name": "Dance Floor",

    "description":
    """You are dancing on the dancefloor with your friends. 
    You feel very hyper and excited after dancing.
    Where would you like to go after dancing? 
    You can go northwest to the outside, west to the Bar1, southwest to the bar2, south to the Balcony, east to the toliet or north to the food. """,

    "exits": {"west": "Bar1", "south": "Balcony", "northwest": "Outside", "north": "Food", "southwest": "Bar2", "east": "Toilet"},
    "time_cost": {"west": 2, "south": 4, "northwest": 3, "north": 4, "southwest": 7, "east": 7},

    "items": [],
    "consumables": []
}

room_food = {
    "name": "Food",

    "description":
    """You smell the yummy food. Would you like to get a burger for £3? You can go south to the Dancefloor or eat a burger.""",

    "exits": {"south": "Dancefloor"},
    "time_cost": {"south": 4},

    "items": [],
    "consumables": [consumables.food_burger]
}

room_taly = {
    "name": "Talybont",

    "description":
    """You are in Talybont North having pre drinks.""",

    "exits": {"south": "Taxi"},
    "time_cost": {"south": 2},

    "items": [item_keys, item_driving_license, item_money, item_id],
    "consumables": []
}

room_taxi = {
    "name": "Taxi",

    "description":
    """You are in a taxi. You can go south to the outside of the SU or go north to Talybont.""",

    "exits": {"south": "Outside", "north": "Talybont"},
    "time_cost": {"south": 15, "north": 15},
    "money_cost": {"south": 8, "north": 8},
    "items": [],
    "consumables": []
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
