import sys

def collatz(number):
    while number != 1:
        if number == 1:
            print(str(number))
        if number % 2 == 0:
            # print(str(number) + ' // 2 = ' + str(number//2))
            number = number // 2
            print(str(number))
        elif number % 2 == 1:
            # print('3 * ' + str(number) + ' + 1 = ' + str(3 * number + 1))
            number = 3 * number + 1
            print(str(number))

print('Enter a number:')
try:
    number = int(input())
except ValueError:
    print('Not a number')
    sys.exit()

try:
    collatz(number)
except:
    print('Something went wrong')
    sys.exit()