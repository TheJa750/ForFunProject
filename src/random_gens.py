import random

def get_starting_stats(points=45):
    stats = ["str", "agi", "con", "wis", "luck"]
    strength = 1
    agility = 1
    constitution = 1
    wisdom = 1
    luck = 1
    
    stat_list = random.choices(stats, k=points)

    for item in stat_list:
        if item == "str":
            strength += 1
        elif item == "agi":
            agility += 1
        elif item == "con":
            constitution += 1
        elif item == "wis":
            wisdom += 1
        elif item == "luck":
            luck += 1
    
    return [strength, agility, constitution, wisdom, luck]
