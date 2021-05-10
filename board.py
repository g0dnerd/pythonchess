class Board:

	import numpy as np

	pieces = list()
	pieces = [
		['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
		['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
		['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
		['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
	]

	def __init__(self, whiteCanCastle, blackCanCastle):

		self.whiteCanCastle = whiteCanCastle
		self.blackCanCastle = blackCanCastle
