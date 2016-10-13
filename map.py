from items import *

room_outside = {
    "name": "Outside",

    "description":
    """You are waiting outside in a masssive queue. You know
    tonight will be good. """,

    "exits": {"south": "Dancefloor", "east": "Food"},

    "items": []
}

room_bar1 = {
    "name": "Bar1",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"east": "Dancefloor", "south": "Bar2"},

    "items": [item_drink]
}

room_bar2 = {
    "name": "Bar2",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"east": "Bar3", "east": "Balcony", "north": "Bar1"},

    "items": [item_wine]
}

room_bar3 = {
    "name": "Bar3",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"north": "Balcony", "east": "Toilet", "west": "Bar2"},

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

    "items": []
}

room_balcony = {
    "name": "Balcony",

    "description":
    """You are standing in the cool breeze of the wind.
    blah blah blah""",

    "exits": {"east": "Toilet", "south": "Bar3", "west": "Bar2", "north": "Dancefloor"},

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

    "items": [item_screen]
}

room_food = {
    "name": "Food",

    "description":
    """You smell the food yum.""",

    "exits": {"south": "Stage", "west": "Outside"},

    "items": [item_chips]
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
    "Toilet": room_toilet
    
}
