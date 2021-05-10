import numpy as np
import config

class boardState:

	board = list()
	moveCount = 0

	board = [
		['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
		['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
		['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]


	def __init__(self, whiteCanCastle, blackCanCastle, toMove):
		self.whiteCanCastle = whiteCanCastle
		self.blackCanCastle = blackCanCastle
		#  white to move = -1, black to move = 1
		self.toMove = toMove


	def print_board(self):
		print("  a b c d e f g h")
		for i in range(8):
			print(8 - i, end = " ")
			for j in range(8):
				if j < 7:
					print(self.board[7-i][j], end = " ")
				else:
					print(self.board[7-i][j])
		print("")


	def make_move(self, userMove):
		# TODO: Decoding Logic for algebraic notation
		# TODO: check move legality
		print("Making move " + userMove)

		# if move length is = 2, it's a non-capturing pawn move
		if len(userMove) == 2:
			# TODO
			moveToRow = int(userMove[1])
			moveToRow-=1
			moveToFile = ord(userMove[0]) - 97
			if self.board[moveToRow+self.toMove][moveToFile].lower() == 'p':
				self.board[moveToRow+self.toMove][moveToFile] = 'x'

				if self.toMove == -1:
					self.board[moveToRow][moveToFile] = 'P'
				else:
					self.board[moveToRow][moveToFile] = 'p'

			elif self.board[moveToRow+(self.toMove*2)][moveToFile].lower() == 'p':
				self.board[moveToRow+(self.toMove*2)][moveToFile] = 'x'

				if self.toMove == -1:
					self.board[moveToRow][moveToFile] = 'P'
				else:
					self.board[moveToRow][moveToFile] = 'p'

		if self.toMove == -1:
			self.toMove = 1
		else:
			self.toMove = -1

		self.print_board()


	# def is_check(self):
		# TODO: Logic for check detection


def main():
	print("Welcome to pychess.")
	print("You are playing as WHITE")
	print("")
	config.moveCount = 0
	gameState = boardState(True, True, -1)
	print(gameState.toMove)
	gameState.print_board()
	for i in range(5):
		userInput = input("Please enter your move: ")
		gameState.make_move(userInput)


if __name__ == "__main__":
	main()

