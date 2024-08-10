board1 = [
    ['X', ' ', ' '],
    ['X', ' ', ' '],
    ['X', ' ', ' ']
]

board2 = [
    ['X', 'X', 'O'],
    ['X', 'O', ' '],
    ['O', 'X', 'X']
]


def winning(board):
    size = len(board)
    winner = ''
    for i in range(size):
        counter = 0
        for j in range(size):
            if board[0][i] == board[j][i] and board[0][i] != ' ':
                counter += 1
            if counter == size:
                winner = board[0][i]
                return winner
    for i in range(size):
        counter = 0
        for j in range(size):
            if board[i][0] == board[i][j] and board[i][0] != ' ':
                counter += 1
            if counter == size:
                winner = board[i][0]
                return winner
    counting1 = 0
    for i in range(size):
        if board[0][0] == board[i][i] and board[0][0] != ' ':
            counting1 += 1
    if counting1 == size:
        winner = board[0][0]
        return winner

    counting2 = 0
    for i in range(size):
        if board[0][size - 1] == board[i][size - 1 - i] and board[0][size - 1] != ' ':
            counting2 += 1
            print(counting2)
    if counting2 == size:
        winner = board[0][size - 1]
        return winner

    is_draw = True
    for row in board:
        for element in row:
            if element == ' ':
                is_draw = False
    if is_draw:
        return 'remis'
    # return ''


print(winning(board2))

# def winndddding(board):
#     size = len(board)
#     winner = True
#     current_player=''
#     for i in range(size):
#         for j in range(size):
#             if board[0][i] != board[j][i] and board[0][i] != ' ':
#                 winner = False
#     if winner:
#         return current_player
#     # for i in range(len(board)):
#     #     if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
#     #         winner = board[0][i]
#     #     elif board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
#     #         winner = board[i][0]
#
#     is_draw = True
#     for row in board:
#         for element in row:
#             if element == ' ':
#                 is_draw = False
#     if is_draw:
#         return None
#     return ''
