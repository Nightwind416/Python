tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    #   setup blank column list
    colWidths = [0] * len(tableData)
#     print(colWidths)
    #   determine max length word for each column
#     print('determine max length word for each column')
    x = 0
    for nestedList in tableData:
#         print(nestedList)
        max = 0
        for i in nestedList:
#             print(i)
            if len(i) > max:
                max = len(i)
#                 print(max)
            else:
                continue
        colWidths[x] = max
        x += 1
#         print(colWidths)
    #   pad whitespace for each word shorter than max
    print('\npad whitespace for each word shorter than max')
    index = 0
    print(colWidths)
    for nestedList in tableData:
        print('\nNested list # ' + str(index) + ' is: ' + str(nestedList))
        for i in nestedList:
            print('\nword at index ' + str(index) + ' ' + i)
            if len(i) < colWidths[index]:
                print('word is too short, padding...')
#                 print(colWidths[index])
                i = i.rjust(colWidths[index])
                print('padded word is ' + i)
                nestedList[index] = i
            else:
                continue
#         print(i)
        index += 1
#         print(nestedList)
    

printTable()