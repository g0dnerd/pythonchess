class Pawn:

	def __init__(self, color, file, row):
		self.color = color
		self.file = file
		self.row = row


	def can_reach(self, file, row):
		# TODO: blocked squares
		if self.row != row:
			return False
		else:
			if self.color == "black":
				if row == 4:
					if self.row == 6:
						return True
					else:
						return False
				elif row - self.row == 1:
					return True
				else:
					return False
			else:
				if row == 3:
					if self.row == 1:
						return True
					else:
						return False
				elif row - self.row == 1:
					return True
				else:
					return False

	# def can_capture(self, file, row):
		#TODO: regular taking, en passant, capture into promotion


class BoardState:

	board = list()
	moveCount = 0


	def __init__(self, whiteCanCastle, blackCanCastle, toMove):
		self.whiteCanCastle = whiteCanCastle
		self.blackCanCastle = blackCanCastle
		#  white to move = -1, black to move = 1
		self.toMove = toMove

	def init_board(self):

		a1 = Rook(0,0)
		h1 = Rook(7,0)
		b1 = Knight(1,0)
		g1 = Knight(6,0)
		c1 = Bishop(2,0)
		f1 = Bishop(5,0)
		d1 = Queen(3,0)
		e1 = King(4,0)

		a8 = Rook(0,7)
		h8 = Rook(7,7)
		b8 = Knight(1,7)
		g8 = Knight(6,7)
		c8 = Bishop(2,7)
		f8 = Bishop(5,7)
		d8 = Queen(3,7)
		e8 = King(4,7)

		a2 = Pawn(0,1)
		b2 = Pawn(1,1)
		c2 = Pawn(2,1)
		d2 = Pawn(3,1)
		e2 = Pawn(4,1)
		f2 = Pawn(5,1)
		g2 = Pawn(6,1)
		h2 = Pawn(7,1)

		a7 = Pawn(0,6)
		b7 = Pawn(1,6)
		c7 = Pawn(2,6)
		d7 = Pawn(3,6)
		e7 = Pawn(4,6)
		f7 = Pawn(5,6)
		g7 = Pawn(6,6)
		h7 = Pawn(7,6)

		self.board = [
			[a1, a2, a3, a4, a5, a6, a7, a8],
			[b1, b2, b3, b4, b5, b6, b7, b8]

	def print_board(self):
		# prints the board upside down since it's stored in a list starting at a1
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

		print("Making move " + userMove)
		# if move length is = 2, it's a non-capturing pawn move
		if len(userMove) == 2:
			moveToRow = int(userMove[1])
			moveToRow -= 1
			# uses the target square's ASCII value to determine the File to move to
			moveToFile = ord(userMove[0]) - 97
			print(moveToRow)
			print(moveToFile)
			# tries to find a pawn to move one square down and moves it
			if self.board[moveToRow+self.toMove][moveToFile].lower() == 'p':
				self.board[moveToRow+self.toMove][moveToFile] = '.'

				if self.toMove == -1:
					self.board[moveToRow][moveToFile] = 'P'
				else:
					self.board[moveToRow][moveToFile] = 'p'

			# else tries to find a pawn two squares down and moves it
			# TODO: only allow for pawns that have not been moved yet.
			elif self.board[moveToRow+(self.toMove*2)][moveToFile].lower() == 'p':
				self.board[moveToRow+(self.toMove*2)][moveToFile] = '.'

				if self.toMove == -1:
					self.board[moveToRow][moveToFile] = 'P'
				else:
					self.board[moveToRow][moveToFile] = 'p'

		# pass the turn to the other player
		if self.toMove == -1:
			self.toMove = 1
		else:
			self.toMove = -1

		self.moveCount += 1
		self.print_board()


# def is_legal(self, move):
	#TODO: legality detection
	#does it move into check/discoveries?
	#can the targeted piece reach the targeted square?
	#is the castling attempt legal?


def main():
	print("Welcome to pychess.")
	print("You are playing as WHITE")
	print("")
	testPawn = Pawn("White", 1,3)
	print(testPawn.can_reach(5,3))
	gameState = BoardState(True, True, -1)
	gameState.moveCount = 0
	gameState.print_board()
	for i in range(5):
		print("Move " + str(gameState.moveCount + 1))
		userInput = input("Please enter your move: ")
		gameState.make_move(userInput)


if __name__ == "__main__":
	main()


