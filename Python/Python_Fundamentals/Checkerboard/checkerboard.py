#DEMO1
def print_board(m,n):
    print('\n'.join(''.join(str((i+j)%2) for i in range(n)) for j in range(m)))
print_board(10,15)

#DEMO2
def checkerboard(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append((i+j) % 2)
    return board

for row in checkerboard(8):
    print(row)

#DEMO3
def print_board(width):
    print ('0 1 ' * (width // 2) + '\n' + '1 0 ' * (width // 2) + '\n') * (width // 2)
print_board(10)

#MYCODE
def star_board(width):
    print ('* ' * (width // 2) + '\n' + ' *' * (width // 2) + '\n') * (width // 2)

star_board(10)