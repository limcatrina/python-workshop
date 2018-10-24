def print_board(board):

	print("The board looks like this: \n")

	for i in range(3):
		print(" ", end=' ')
		for j in range(3):
			if board[i*3+j] == 1:
				print('X', end=' ')
			elif board[i*3+j] == 0:
				print('O', end=' ')
			elif board[i*3+j] != -1:
				print((board[i*3+j] - 1), end=' ')
			else:
				print(' ', end=' ')

			if j != 2:
				print(" | ", end=' ')
		print()

		if i != 2:
			print("-----------------")
		else:
			print()

def print_instruction():
	#reserve 0 and 1 values to indicate player choice
	print("Please use the following cell numbers to make your move")
	print_board([2,3,4,5,6,7,8,9,10])


def get_input(user):
	valid = False
	while not valid:
		try:
			tile_choice = input("Where would you like to place " + user + " (1-9)? ")
			tile_choice = int(tile_choice)
			if tile_choice >= 1 and tile_choice <= 9:
				return tile_choice-1
			else:
				print("That is not a valid move! Please try again.\n")
				print_instruction()
		except:
			print(tile_choice + " is not a valid move! Please try again.\n")

def check_win(board):
	win_cond = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
	for each in win_cond:
		try:
			if board[each[0] - 1] == board[each[1] - 1] and board[each[1] - 1] == board[each[2] - 1]:
				return board[each[0]]
		except:
			print("Error")
	return -1

def run_turns(board, move):
	# print board
	print_board(board)
	print("Turn number " + str(move+1))
	if move % 2 == 0:
		user = 'X'
	else:
		user = 'O'

	#get user input
	tile_choice = get_input(user)
	while board[tile_choice] != -1:
		print("Invalid move! Cell already taken. Please try again.\n")
		tile_choice = get_input(user)
	board[tile_choice] = 1 if user == 'X' else 0

	#run move, check for end game
	move += 1
	if move > 4:
		winner = check_win(board)
		if winner != -1:
			out = "The winner is "
			out += "X" if winner == 1 else "O"
			out += " :)"
			quit_game(board,out)
		elif move == 9:
			quit_game(board,"No winner :(")
	return move


def quit_game(board,msg):
	print_board(board)
	print(msg)
	quit()

def main():
	# print instructions
	# setup game
	# alternate turn
	# check if win or end
	# quit and show the board

	print_instruction()
	move = 0
	board = []
	for i in range(9):
		board.append(-1)

	loop_runner = False
	while not loop_runner:
		move = run_turns(board, move)

if __name__ == "__main__":
	main()
