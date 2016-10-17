from items import *

room_outside = {
    "name": "Outside",

    "description":
    """You are waiting outside in a massive queue. You know
    tonight will be good. """,

    "exits": {"south": "Dancefloor", "east": "Food", "north": "Taxi"},
    "time_cost": {"south": 2, "east": 10, "north": 2},
    "items": []
}

room_bar1 = {
    "name": "Bar1",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"east": "Dancefloor", "south": "Bar2"},
    "time_cost": {"east": 2, "south": 10},

    "items": [item_drink]
}

room_bar2 = {
    "name": "Bar2",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"east": "Balcony", "north": "Bar1"},
    "time_cost": {"east": 2, "north": 10},

    "items": [item_wine]
}

room_bar3 = {
    "name": "Bar3",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"north": "Balcony", "east": "Toilet", "west": "Bar2"},
    "time_cost": {"north": 8, "east": 7, "west": 11},

    "items": [item_wine]
}

room_toilet = {
    "name": "Toilet",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Bar3"},
    "time_cost": {"west": 5},
    "items": []
}

room_balcony = {
    "name": "Balcony",

    "description":
    """You are standing in the cool breeze of the wind.
    blah blah blah""",

    "exits": {"east": "Toilet", "south": "Bar3", "west": "Bar2", "north": "Dancefloor"},
    "time_cost": {"east": 7, "south": 10, "west": 15, "north": 4},
    "items": [item_flower]
}


room_dancefloor = {
    "name": "Dance Floor",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Bar1", "south": "Balcony", "north": "Stage"},
    "time_cost": {"west": 10, "south": 4, "north": 3},

    "items": []
}

room_stage = {
    "name": "Stage",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Food", "south": "Dancefloor", "west": "Bar1"},
    "time_cost": {"north": 2, "south": 1, "west": 10},

    "items": [item_screen]
}

room_food = {
    "name": "Food",

    "description":
    """You smell the food yum.""",

    "exits": {"south": "Stage", "west": "Outside"},
    "time_cost": {"south": 2, "west": 3},

    "items": [item_chips]
}

room_taly = {
    "name": "Talybont",

    "description":
    """You are in Talybont North having pre drinks.""",

    "exits": {"south": "Outside"},
    "time_cost": {"south": 20},

    "items": [item_drink]
}

room_taxi = {
    "name": "Taxi",

    "description":
    """You are in taxi.""",

    "exits": {"south": "Outside", "north": "Dancefloor"},
    "time_cost": {"south": 5, "north": 15},
    "money_cost": {"south": 12, "north": 12},
    "items": []
}

rooms = {
    "Dancefloor": room_dancefloor,
    "Outside": room_outside,
    "Food": room_food,
    "Stage": room_stage,
    "Bar1": room_bar1,
    "Bar2": room_bar2,
    "Bar3": room_bar3,
    "Balcony": room_balcony,
    "Toilet": room_toilet,
    "Talybont": room_taly,
    "Taxi": room_taxi
    
}
