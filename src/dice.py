import random

class Die():
    def __init__(self, state):
        self.state = state

die_0 = Die(0)
die_1 = Die(0)
die_2 = Die(0)
die_3 = Die(0)

def roll(die):
    die.state = random.randint(1, 4)

def roll_all():
    roll(die_0)
    roll(die_1)
    roll(die_2)
    roll(die_3)