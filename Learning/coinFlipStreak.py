# Coin Flip Streak

import random

listStreak = 0
totalStreaks = 0

for experimentNumber in range(10000):
    print('Experiment #: ' + str(experimentNumber))
    flipList = []
    count = 0
    # Code that creates a list of 100 'heads' or 'tails' values.
    for x in range(100):
        flip = random.choice(['Heads', 'Tails'])
#         print(flip)
        flipList.append(flip)
    else:
#         print('Flip list = ' + str(flipList))
    # Code that checks if there is a streak of 6 heads or tails in a row.
        previous = 'none'
    for x in flipList:
        if previous == 'none':
            print('Initial check')
        elif x == previous:
            count += 1
#             print('Current streak count = ' + str(count))
        else:
            if count >= 6:
                listStreak += 1
                count = 0
                print('Experiment # ' + str(experimentNumber) + ' has a streak!')
            else:
                count = 0
#                 print('Experiment # ' + str(experimentNumber) + ' does not have a streak!')
        previous = x
    if listStreak >= 1:
        totalStreaks += 1
        listStreak = 0
        print('Adding streak count')
    else:
        print('Keeping streak count')
        continue
# Print results
#     print('Experiment #: ' + str(experimentNumber))
#     print('Flip list = ' + str(flipList))
    print('Total Streaks = ' + str(totalStreaks))
    print('')
    
    
    
    
    

print('Chance of streak: %s%%' % (totalStreaks / 100))