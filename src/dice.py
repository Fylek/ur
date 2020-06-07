import random

class Die():
    def __init__(self, state):
        self.state = state

die_list = [
    Die(0),
    Die(0),
    Die(0),
    Die(0)
]

def roll(die):
    die.state = random.randint(0, 1)

def roll_all():
    roll(die_list[0])
    roll(die_list[1])
    roll(die_list[2])
    roll(die_list[3])