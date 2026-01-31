import random
dice_quality = int(input("enter the number of dices want to roll: "))
total = 0

for i in range(dice_quality):
    roll = random.randint(1,6)
    total += roll

print(f"total sums of dice rolls are {total}.")