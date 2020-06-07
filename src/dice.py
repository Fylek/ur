import random

class Die():
    def __init__(self, state):
        self.state = state

die_0 = Die(0)
die_1 = Die(0)
die_2 = Die(0)
die_3 = Die(0)

die_list = [
    die_0,
    die_1,
    die_2,
    die_3
]

def roll(die):
    die.state = random.randint(0, 1)

def roll_all():
    roll(die_list[0])
    roll(die_list[1])
    roll(die_list[2])
    roll(die_list[3])