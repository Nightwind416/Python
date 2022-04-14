# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#   Print grid
x = 0
y = 0
print('Grid')
print('')
while x < 9:
    while y < 6:
        print(grid[x][y], end="")
        y += 1
    x += 1
    y = 0
    print('')

    
#   Print rotated grid
x = 0
y = 0
print('')
print('')
print('Rotated')
print('')

while y < 6:
    while x < 9:
        print(grid[x][y], end="")
        x += 1
    y += 1
    x = 0
    print('')