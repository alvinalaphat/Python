from __future__ import print_function

from IPython.display import clear_output



answer = input('do you want to play? ')

if answer == 'yes':

    print("OK let's play")

else:

    print('Well ok, see ya!')

    exit()



board = [' '] * 10



def display_board(board):



    clear_output()

    print('   |   |')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('   |   |')



display_board(board)

answer = []



while (answer != 'X' and answer != 'O'):

    answer = input('Player 1, do you want to be X or O? ').upper()

    continue

if answer == 'O':

    print("OK then Player 2 will be X")

    p1 = 'O'

    p2 = 'X'

else:

    print("OK then Player 2 will be O")

    p1 = 'X'

    p2 = 'O'

answer = clear_output



num1 = int(input('Player 1, make your move: '))

board[num1] = p1

display_board(board)



num2 = int(input('Player 2, make your move: '))

board[num2] = p2

display_board(board)



num1 = int(input('Player 1, make your move: '))

board[num1] = p1

display_board(board)



num2 = int(input('Player 2, make your move: '))

board[num2] = p2

display_board(board)



num1 = int(input('Player 1, make your move: '))

board[num1] = p1

display_board(board)

if p1 == board[1] == board[2] == board[3] or p1 == board[4] == board[5] == board[6] or p1 == board[7] == board[8] == board[9] or p1 == board[1] == board[5] == board[9] or p1 == board[3] == board[5] == board[7] or p1 == board[1] == board[4] == board[7] or p1 == board[2] == board[5] == board[8] or p1 == board[3] == board[6] == board[9]:

	print('Player 1 wins!')

	exit()

if p2 == board[1] == board[2] == board[3] or p2 == board[4] == board[5] == board[6] or p2 == board[7] == board[8] == board[9] or p2 == board[1] == board[5] == board[9] or p2 == board[3] == board[5] == board[7] or p2 == board[1] == board[4] == board[7] or p2 == board[2] == board[5] == board[8] or p2 == board[3] == board[6] == board[9]:

	print('Player 2 wins!')

	exit()



num2 = int(input('Player 2, make your move: '))

board[num2] = p2

display_board(board)

if p1 == board[1] == board[2] == board[3] or p1 == board[4] == board[5] == board[6] or p1 == board[7] == board[8] == board[9] or p1 == board[1] == board[5] == board[9] or p1 == board[3] == board[5] == board[7] or p1 == board[1] == board[4] == board[7] or p1 == board[2] == board[5] == board[8] or p1 == board[3] == board[6] == board[9]:

	print('Player 1 wins!')

	exit()

if p2 == board[1] == board[2] == board[3] or p2 == board[4] == board[5] == board[6] or p2 == board[7] == board[8] == board[9] or p2 == board[1] == board[5] == board[9] or p2 == board[3] == board[5] == board[7] or p2 == board[1] == board[4] == board[7] or p2 == board[2] == board[5] == board[8] or p2 == board[3] == board[6] == board[9]:

	print('Player 2 wins!')

	exit()



num1 = int(input('Player 1, make your move: '))

board[num1] = p1

display_board(board)

if p1 == board[1] == board[2] == board[3] or p1 == board[4] == board[5] == board[6] or p1 == board[7] == board[8] == board[9] or p1 == board[1] == board[5] == board[9] or p1 == board[3] == board[5] == board[7] or p1 == board[1] == board[4] == board[7] or p1 == board[2] == board[5] == board[8] or p1 == board[3] == board[6] == board[9]:

	print('Player 1 wins!')

	exit()

if p2 == board[1] == board[2] == board[3] or p2 == board[4] == board[5] == board[6] or p2 == board[7] == board[8] == board[9] or p2 == board[1] == board[5] == board[9] or p2 == board[3] == board[5] == board[7] or p2 == board[1] == board[4] == board[7] or p2 == board[2] == board[5] == board[8] or p2 == board[3] == board[6] == board[9]:

	print('Player 2 wins!')

	exit()



num2 = int(input('Player 2, make your move: '))

board[num2] = p2

display_board(board)

if p1 == board[1] == board[2] == board[3] or p1 == board[4] == board[5] == board[6] or p1 == board[7] == board[8] == board[9] or p1 == board[1] == board[5] == board[9] or p1 == board[3] == board[5] == board[7] or p1 == board[1] == board[4] == board[7] or p1 == board[2] == board[5] == board[8] or p1 == board[3] == board[6] == board[9]:

	print('Player 1 wins!')

	exit()

if p2 == board[1] == board[2] == board[3] or p2 == board[4] == board[5] == board[6] or p2 == board[7] == board[8] == board[9] or p2 == board[1] == board[5] == board[9] or p2 == board[3] == board[5] == board[7] or p2 == board[1] == board[4] == board[7] or p2 == board[2] == board[5] == board[8] or p2 == board[3] == board[6] == board[9]:

	print('Player 2 wins!')

	exit()



num1 = int(input('Player 1, make your move: '))

board[num1] = p1

display_board(board)

if p1 == board[1] == board[2] == board[3] or p1 == board[4] == board[5] == board[6] or p1 == board[7] == board[8] == board[9] or p1 == board[1] == board[5] == board[9] or p1 == board[3] == board[5] == board[7] or p1 == board[1] == board[4] == board[7] or p1 == board[2] == board[5] == board[8] or p1 == board[3] == board[6] == board[9]:

	print('Player 1 wins!')

	exit()

if p2 == board[1] == board[2] == board[3] or p2 == board[4] == board[5] == board[6] or p2 == board[7] == board[8] == board[9] or p2 == board[1] == board[5] == board[9] or p2 == board[3] == board[5] == board[7] or p2 == board[1] == board[4] == board[7] or p2 == board[2] == board[5] == board[8] or p2 == board[3] == board[6] == board[9]:

	print('Player 2 wins!')

	exit()

else:

	print("It's a draw!")

	exit()
