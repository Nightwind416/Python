# Coin Flip Streak

import random

numberOfStreaks = 0

for experimentNumber in range(2):
    toss = []
    count = 0
    # Code that creates a list of 100 'heads' or 'tails' values.
    for x in range(100):
        flip = random.choice(['Heads', 'Tails'])
#         print(flip)
        toss.append(flip)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    
    
    
    
# print(toss)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))