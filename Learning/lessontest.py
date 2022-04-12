spam = ['apples', 'bananas', 'tofu', 'cats', 'birds', 'tigers', 'lions']

# Comma Code

print('list = ' + str(spam))
number = len(spam)

print('"The list is ', end = '')

if number == 0:
    print('empty"')
#     quit()

elif number == 1:
    print('just ' + str(spam[0]) + '"')
#     quit()

elif number == 2:
    print(spam[0] + ' and ' + spam[1] + '"')
#     quit()

else:
    for x in spam:
        if number == 1:
            print('and ' + str(x), end = '')
        else:
            print(str(x) + ', ', end = '')
            number -= 1
    print('"')