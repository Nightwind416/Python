# Rock, Paper, Scissors, Lizard, Spock

import random
import sys

print('Rock, Paper, Scissors, Lizard, Spock')

# These variables keep track of the number of wins, losses, and ties.
win_Total = 0
loss_Total = 0
tie_Total = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (win_Total, loss_Total, tie_Total))
    while True:  # The player input loop.
        print('Enter your move: rock, paper, scissors, lizard, spock, or quit')
        playerMove = input()
        if playerMove == 'quit':
            sys.exit()  # Quit the program.
        if playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissors' or playerMove == 'lizard' or playerMove == 'spock':
            break  # Break out of the player input loop.
        print('Type one of rock, paper, scissors, lizard, spock, or quit.')

    # Display what the player chose:
    if playerMove == 'rock':
        print('ROCK versus...')
    elif playerMove == 'paper':
        print('PAPER versus...')
    elif playerMove == 'scissors':
        print('SCISSORS versus...')
    elif playerMove == 'lizard':
        print('SCISSORS versus...')
    elif playerMove == 'spock':
        print('SPOCK versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'rock'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'paper'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 'scissors'
        print('SCISSORS')
    elif randomNumber == 4:
        computerMove = 'lizard'
        print('LIZARD')
    elif randomNumber == 5:
        computerMove = 'spock'
        print('SPOCK')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        tie_Total = tie_Total + 1
    # Checks when player chooses rock
    elif playerMove == 'rock' and computerMove == 'scissors' or computerMove == 'lizard':
        print('You win!')
        win_Total = win_Total + 1
    elif playerMove == 'rock' and computerMove == 'paper' or computerMove == 'spock':
        print('You lose!')
        loss_Total = loss_Total + 1
    # Checks whecn player chooses paper
    elif playerMove == 'paper' and computerMove == 'rock' or computerMove == 'spock':
        print('You win!')
        win_Total = win_Total + 1
    elif playerMove == 'paper' and computerMove == 'scissors' or computerMove == 'lizard':
        print('You lose!')
        loss_Total = loss_Total + 1
    # Checks whecn player chooses scissors
    elif playerMove == 'scissors' and computerMove == 'paper' or computerMove == 'lizard':
        print('You win!')
        win_Total = win_Total + 1
    elif playerMove == 'scissors' and computerMove == 'rock' or computerMove == 'spock':
        print('You lose!')
        loss_Total = loss_Total + 1
    # Checks whecn player chooses lizard
    elif playerMove == 'lizard' and computerMove == 'paper' or computerMove == 'spock':
        print('You win!')
        win_Total = win_Total + 1
    elif playerMove == 'lizard' and computerMove == 'rock' or computerMove == 'scissors':
        print('You lose!')
        loss_Total = loss_Total + 1
    # Checks whecn player chooses spock
    elif playerMove == 'spock' and computerMove == 'scissors' or computerMove == 'rock':
        print('You win!')
        win_Total = win_Total + 1
    elif playerMove == 'spock' and computerMove == 'paper' or computerMove == 'lizard':
        print('You lose!')
        loss_Total = loss_Total + 1
