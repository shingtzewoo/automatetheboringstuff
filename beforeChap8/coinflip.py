# Write your code here :-)
import random
numberOfStreaks = 0
for experimentNumber in range(1000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    items = []
    counterH = 0
    counterT = 0
    for i in range(100):
        if random.randint(0, 1) == 0:
            items.append('H')
            counterH += 1
            counterT = 0
            if counterH == 6:
                numberOfStreaks += 1
                counterH = 0
        else:
            items.append('T')
            counterT += 1
            counterH = 0
            if counterT == 6:
                numberOfStreaks += 1
                counterT = 0
print('Chance of streak out of 10,000 x 100 tries: %s%%' % (numberOfStreaks / 1000))