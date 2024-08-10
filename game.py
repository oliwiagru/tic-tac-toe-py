import datetime
import random

print("          Tic Tac Toe")
board_size = int(input('Enter size of the board (3-5): '))
rounds_number = int(input('Enter number of rounds you want to play: '))
nickname = input('Enter your nickname: ')
input('Press enter to start the game!')


def create_board(size):
    board = []
    for i in range(size):
        row = [' '] * size
        board.append(row)
    return board


def render_board(board):
    for row in board:
        print(row)
    print()


def coordinates_o(board, size):
    print('Please enter row and and column you want to choose')
    # try:
    row = int(input('row: '))
    while row > size:
        print(f'Enter the number from the range from 1 to {size}!')
        row = int(input('row: '))
    column = int(input('column: '))
    while column > size:
        print(f'Enter the number from the range from 1 to {size}!')
        column = int(input('column: '))
    while board[row - 1][column - 1] != ' ':
        print('Indicated field on the board is already occupied. Choose another one!')
        row = int(input('row: '))
        column = int(input('column: '))
    board[row - 1][column - 1] = 'O'
    # except ValueError:
    #     print('Invalid value. Please enter a number.')


def coordinates_x(board, size):
    row = random.randint(0, size - 1)
    column = random.randint(0, size - 1)
    while board[row][column] != ' ':
        row = random.randint(0, size - 1)
        column = random.randint(0, size - 1)
    else:
        board[row][column] = 'X'


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
    if counting2 == size:
        winner = board[0][size - 1]
        return winner

    is_draw = True
    for row in board:
        for element in row:
            if element == ' ':
                is_draw = False
    if is_draw:
        return None
    return ''


tournament = []


def save_round_data(nickname, winner, time, board):
    tournament.append({'nickname': nickname, 'symbol': winner, 'time': time, 'board': board})


for i in range(rounds_number):
    print(f'ROUND {i + 1}')
    game_board = create_board(board_size)
    render_board(game_board)

    is_game_running = True
    current_player = 'O'
    while is_game_running:
        if current_player == 'O':
            coordinates_o(game_board, board_size)
            current_player = 'X'
        else:
            coordinates_x(game_board, board_size)
            current_player = 'O'
        render_board(game_board)

        winner = winning(game_board)
        if winner == 'O' or winner == 'X':
            print(f'{winner} is a winner! Game over!')
            current_time = datetime.datetime.now()
            save_round_data(nickname, winner, current_time, game_board)
            is_game_running = False
            print()

        elif winner is None:
            print('Draw! Game over!')
            current_time = datetime.datetime.now()
            save_round_data(nickname, winner, current_time, game_board)
            is_game_running = False
            print()

print(tournament)
