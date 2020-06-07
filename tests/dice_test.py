import dice

# Roll all dice, one by one
print("----- INDIVIDUAL ROLLS -----")
for x in range(0, 4):
    dice.die_list[x].roll()
    print(f"Die {x}: {dice.die_list[x].state}")

# Test the roll_all function
print("----- GROUP ROLL -----")
dice.roll_all()
for x in range(0, 4):
    print(f"Die {x}: {dice.die_list[x].state}")



