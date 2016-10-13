from items import *

room_outside = {
    "name": "Outside",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Dancefloor", "east": "Food"},

    "items": [item_biscuits, item_handbook]
}

room_bar1 = {
    "name": "Bar1",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

    "exits":  {"east": "Dancefloor", "south": "Bar2"},

    "items": []
}

room_bar2 = {
    "name": "Bar2",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"east": "bar3", "east": "balcony", "north": "bar1"},

    "items": []
}

room_bar3 = {
    "name": "Bar3",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"north": "balcony", "east": "toilet", "west": "bar2"},

    "items": []
}

room_toilet = {
    "name": "Toilet",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "balcony", "west": "bar3"},

    "items": [item_pen]
}

room_balcony = {
    "name": "Balcony",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"east": "toilet", "south": "bar3", "west": "bar2", "north": "dancefloor"}

    "items": [item_pen]
}


room_dancefloor = {
    "name": "Dance Floor",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "bar1", "south": "balcony", "north": "stage"},

    "items": [item_pen]
}

room_stage = {
    "name": "Stage",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "food", "south": "dancefloor", "west": "bar1"}

    "items": [item_pen]
}

room_food = {
    "name": "Food",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"south": "stage", "west": "outside"},

    "items": [item_pen]
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
