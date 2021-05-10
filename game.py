import numpy as np
import config

class boardState:

	board = list()
	moveCount = 0

	board = [
		['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
		['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
		['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]


	def __init__(self, whiteCanCastle, blackCanCastle):
		self.whiteCanCastle = whiteCanCastle
		self.blackCanCastle = blackCanCastle


	def printBoard(self):
		print("  A B C D E F G H")
		for i in range(8):
			print(8 - i, end = " ")
			for j in range(8):
				if j < 7:
					print(self.board[i][j], end = " ")
				else:
					print(self.board[i][j])


	def make_move(self, inputString):
		# TODO: Decoding Logic for algebraic notation
		print("Move " + str(moveCount) + ":")


def main():
	print("Welcome to pychess.")
	print("You are playing as WHITE")
	print("")
	config.moveCount = 0
	gameState = boardState(True, True)
	gameState.printBoard()

if __name__ == "__main__":
	main()

