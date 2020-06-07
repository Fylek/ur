import dice

# Roll all dice, one by one
dice.roll(dice.die_0)
print(dice.die_list[0].state)
dice.roll(dice.die_list[1])
print(dice.die_list[1].state)
dice.roll(dice.die_list[2])
print(dice.die_list[2].state)
dice.roll(dice.die_list[3])
print(dice.die_list[3].state)