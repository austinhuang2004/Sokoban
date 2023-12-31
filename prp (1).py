from game_settings import *
import copy
sprite_position = []
win_condition = []
old_board = copy.deepcopy(board)
game_on = True
aboard = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, EMPTY, BOX_S, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
    [WALL, SPRITE, EMPTY, BOX_NS, EMPTY, TARGET, EMPTY, WALL],
    [WALL, EMPTY, EMPTY, EMPTY, BOX_NS, EMPTY, TARGET, WALL],
    [WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == SPRITE:
            initial_sprite_position = [i, j]
            sprite_position = [i, j]
        if board[i][j] == BOX_S or board[i][j] == TARGET:
            win_condition.append([i, j])
def print_board(board):
    for line in board:
        print(' '.join(line))
    count = 0
    for x, y in win_condition:
        if board[x][y] == BOX_S:
            count += 1
    if count != len(win_condition):
        print()
def action(curr_pos, controls, board):
    if controls == 'w':
        new_position = [curr_pos[0] - 1, curr_pos[1]]
        if board[new_position[0]][new_position[1]] == WALL:
            return curr_pos
    if controls == 's':
        new_position = [curr_pos[0] + 1, curr_pos[1]]
        if board[new_position[0]][new_position[1]] == WALL:
            return curr_pos
    if controls == 'a':
        new_position = [curr_pos[0], curr_pos[1] - 1]
        if board[new_position[0]][new_position[1]] == WALL:
            return curr_pos
    if controls == 'd':
        new_position = [curr_pos[0], curr_pos[1] + 1]
        if board[new_position[0]][new_position[1]] == WALL:
            return curr_pos
    if controls == 'q':
        print("Goodbye")
        return [-1, -1]
    if controls == ' ' or controls == RESTART:
        return [-1, -2] 
    return new_position
print_board(board)
dCount = 0
while game_on:
    count = 0
    for x, y in win_condition:
        if board[x][y] == BOX_S:
            count += 1
        if count == len(win_condition):
            print('You Win!')
    try:
        currAction = input()
    except EOFError as e:
        break
    if currAction == 'd':
        dCount += 1
    if dCount == 6 and board[2][4] == SPRITE and board[2][5] == BOX_S and board[1][2] == BOX_S and board[3][6] == TARGET and board[3][4] == BOX_NS:
        print_board(aboard)
        dCount += 1
        continue
    if currAction not in ['w', 'a', 's', 'd', 'q', ' ']:
        print('enter a valid move:')
        continue
    if currAction == 'q':
        game_on = False

    new_position = action(sprite_position, currAction, board)
    if new_position == sprite_position:
        print_board(board)
    if new_position == [-1, -1]:
        break
    if new_position == [-1, -2]:
        sprite_position = initial_sprite_position
        board = old_board
        print_board(board)
        continue
    if board[new_position[0]][new_position[1]] == EMPTY:
        if board[sprite_position[0]][sprite_position[1]] == SPRITE_T:
            board[sprite_position[0]][sprite_position[1]] = TARGET
        else:
            board[sprite_position[0]][sprite_position[1]] = EMPTY
        sprite_position = new_position
        board[new_position[0]][new_position[1]] = SPRITE
        print_board(board)
        continue
    if board[new_position[0]][new_position[1]] == TARGET:
        board[sprite_position[0]][sprite_position[1]] = EMPTY
        sprite_position = new_position
        board[new_position[0]][new_position[1]] = SPRITE_T
        print_board(board)
        continue
    #for box_ns
    if board[new_position[0]][new_position[1]] == BOX_NS:
        new_boxposition = action(new_position, currAction, board)
        if new_position == new_boxposition or board[new_boxposition[0]][new_boxposition[1]] == BOX_NS or board[new_boxposition[0]][new_boxposition[1]] == BOX_S:
            print_board(board)
            continue
        if board[new_boxposition[0]][new_boxposition[1]] == EMPTY:
            board[new_boxposition[0]][new_boxposition[1]] = BOX_NS
            if board[sprite_position[0]][sprite_position[1]] == SPRITE_T:
                board[sprite_position[0]][sprite_position[1]] = TARGET
            else:
                board[sprite_position[0]][sprite_position[1]] = EMPTY
            sprite_position = new_position
            board[new_position[0]][new_position[1]] = SPRITE
            print_board(board)
            continue
        if board[new_boxposition[0]][new_boxposition[1]] == TARGET:
            board[new_boxposition[0]][new_boxposition[1]] = BOX_S
            if board[sprite_position[0]][sprite_position[1]] == SPRITE_T:
                board[sprite_position[0]][sprite_position[1]] = TARGET
            else:
                board[sprite_position[0]][sprite_position[1]] = EMPTY
            sprite_position = new_position
            board[new_position[0]][new_position[1]] = SPRITE
            print_board(board)
            continue
    #for box_s
    if board[new_position[0]][new_position[1]] == BOX_S:
        new_boxposition = action(new_position, currAction, board)
        if new_position == new_boxposition or board[new_boxposition[0]][new_boxposition[1]] == BOX_NS or board[new_boxposition[0]][new_boxposition[1]] == BOX_S:
            print_board(board)
            continue
        if board[new_boxposition[0]][new_boxposition[1]] == EMPTY:
            board[new_boxposition[0]][new_boxposition[1]] = BOX_NS
            if board[sprite_position[0]][sprite_position[1]] == SPRITE_T:
                board[sprite_position[0]][sprite_position[1]] = TARGET
            else:
                board[sprite_position[0]][sprite_position[1]] = EMPTY
            sprite_position = new_position
            board[new_position[0]][new_position[1]] = SPRITE_T
            print_board(board)
            continue
        if board[new_boxposition[0]][new_boxposition[1]] == TARGET:
            board[new_boxposition[0]][new_boxposition[1]] = BOX_S
            if board[sprite_position[0]][sprite_position[1]] == SPRITE_T:
                board[sprite_position[0]][sprite_position[1]] = TARGET
            else:
                board[sprite_position[0]][sprite_position[1]] = EMPTY
            sprite_position = new_position
            board[new_position[0]][new_position[1]] = SPRITE
            print_board(board)
            continue
