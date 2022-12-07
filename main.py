board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board2 = [
    [1,6,8,0,0,0,9,0,2],
    [0,0,0,3,0,1,0,0,0],
    [0,3,0,6,2,0,0,0,0],
    [0,0,9,0,0,0,1,0,6],
    [0,0,1,0,0,0,3,7,0],
    [0,4,3,5,0,0,0,0,9],
    [0,0,0,8,0,2,6,0,0],
    [0,0,0,9,0,5,0,2,3],
    [2,0,6,0,3,0,7,0,0]
]

def solve(board):
    pos = find_empty(board)
    if not pos:
        return True

    row,col = pos
    for num in range(1,10):
        if is_valid(board, num, pos):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    # The event that 1-9 does not work in the position, backtrack 
    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None


def is_valid(board, num, pos):
    row,col = pos
    for i in range(len(board[0])):
        if board[row][i] == num and i != col:
            return False
    for i in range(len(board)):
        if board[i][col] == num and i != row:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, (box_y*3)+3):
        for j in range(box_x*3, (box_x*3)+3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        # Every 3 rows divide board
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("  |  ", end="") # Does not go to next line
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board2)
solve(board2)
print("-----------------------")
print_board(board2)
