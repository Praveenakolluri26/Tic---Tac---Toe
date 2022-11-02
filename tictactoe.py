from random import randrange

def display_board(board):
    print("+-------" * 3,"+", sep ="")
    for i in range(3):
        print("|       " * 3,"|", sep ="")
        for j in range(3):
            print("|   " + str(board[i][j]) +"   ",end="")
        print("|")
        print("|       "*3 + "|", sep ="")
        print("+-------"*3 + "+", sep ="")
                  

def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Bad move - repeat your input!")
            continue
        move = int(move) - 1
        i = move // 3
        j = move % 3
        sign = board[i][j]
        ok = sign not in ['O','X']
        if not ok:
            print("Field already occupied - repeat your input!")
            continue
    board[i][j] = 'O'

def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['O','X']:
                free.append((i,j))
    return free

def victory_for(board,sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2-rc][2-rc] != sgn:
            cross2 = False
    if cross1 or cross2 :
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt>0 :
        this = randrange(cnt)
        i,j = free[this]
        board[i][j] = 'X'

board = [[3 * j+i+1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board,'O')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You Won!")
elif victor == 'me' :
    print("I Won!")
else:
    print("Tie!")
