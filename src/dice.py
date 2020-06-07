import random

class Die():
    def __init__(self, state):
        self.state = state
    
    def roll(self):
        self.state = random.randint(0, 1)


die_list = [
    Die(0),
    Die(0),
    Die(0),
    Die(0)
]

def roll_all():
    for x in range(0, 4):
        die_list[x].roll()