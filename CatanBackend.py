"""
Catan Board and Hexagon Classes
Stuart Bradley
23/01/2014
"""

import kivy.graphics as graphics
from random import randint, shuffle

class CatanBoard:

	def __init__(self):
		self.grid = []
		
		self.iniTiles = {"Sheep": 7, "Brick": 7, "Wood": 7, "Ore": 7, "Wheat": 7, "Desert": 5, "Gold": 4}
		self.iniTokens = {"2": 4, "3": 6, "4": 6, "5": 6, "6": 6, "7": 6, "8": 6, "9": 6, "10": 6, "11": 6, "12": 4}
		self.gridWidth = 11
		self.gridHeight = 7
		self.tilePool = self.iniTiles.copy()
		self.tokenPool = self.iniTokens.copy()

		self.players = 6
		self.seafarers = True

	def ini_Grid(self):
		l = []
		for i in range(self.gridWidth):
			l.append([])
			for j in range(self.gridHeight):
				l[i].append(CatanHex(i, j))
				l[i][j].colour = [0.24,0.67,0.81]
		l[0][0] = 'b'
		l[10][0] = 'b'
		l[10][1] = 'b'
		l[10][3] = 'b'
		l[10][5] = 'b'
		l[0][6] = 'b'
		l[10][6] = 'b'
		return l

	def colour_Grid(self, mode):
		self.tilePool = self.iniTiles.copy()
		self.tokenPool = self.iniTokens.copy()

		for i in range(self.gridWidth):
			for j in range(self.gridHeight):
				if self.grid[i][j] != 'b':
					if mode == 'Coastal':
						self.grid[i][j].colour = self.rand_Land_Picker()
					elif mode == 'Thin Land Mass':
						self.grid[i][j].colour = self.rand_Thin_Islands(i, j)
					elif mode == 'Large Land Mass':
						self.grid[i][j].colour = self.rand_Large_Land_Mass(i, j)
					elif mode == 'Large Islands':
						self.grid[i][j].colour = self.rand_Large_Islands(i, j)
					elif mode =='Small Islands':
						self.grid[i][j].colour = self.rand_Small_Islands(i, j)
		if mode == 'Random':
			self.rand_Random()

	#Mode: 0 - creates coastal areas 
	def rand_Land_Picker(self):
		if sum(self.tilePool.values()) > 0:
			number = randint(1,7)
			if number is 1:
				if self.tilePool["Wheat"] > 0:
					self.tilePool["Wheat"] -= 1
					return [0.92,0.72,0.26]
				else: 
					return [0.24,0.67,0.81]
			elif number is 2:
				if self.tilePool["Sheep"] > 0:
					self.tilePool["Sheep"] -= 1
					return [0.65,0.76,0.25]
				else:
					return [0.24,0.67,0.81]
			elif number is 3:
				if self.tilePool["Ore"] > 0:
					self.tilePool["Ore"] -= 1
					return [0.5,0.5,0.5]
				else:
					return [0.24,0.67,0.81]
			elif number is 4:
				if self.tilePool["Wood"] > 0:
					self.tilePool["Wood"] -= 1
					return [0.23,0.44,0.27]
				else:
					return [0.24,0.67,0.81]
			elif number is 5:
				if self.tilePool["Brick"] > 0:
					self.tilePool["Brick"] -= 1
					return [0.9,0.61,0.32]
				else:
					return [0.24,0.67,0.81]
			elif number is 6:
				if self.tilePool["Desert"] > 0:
					self.tilePool["Desert"] -= 1
					return [0.99,0.92,0.77]
				else:
					return [0.24,0.67,0.81]
			elif number is 7:
				if self.tilePool["Gold"] > 0:
					self.tilePool["Gold"] -= 1
					return [0.95,0.95,0]
				else:
					return [0.24,0.67,0.81]
		else:
			return [0.24,0.67,0.81]

	def rand_Thin_Islands(self, i, j):
		if self.grid[i][j] != 'b':
			numb = self.get_Neighbour_Amount(i,j)

			roll = randint(1,6) + randint(1,6)

			if 1 <= roll <= 6:
				return [0.24,0.67,0.81]
			elif roll == 7:
				if numb <= 1:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 8:
				if numb <= 2:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 9:
				if numb <= 3:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 10:
				if numb <= 4:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 11:
				if numb <= 5:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 12:
				if numb <= 6:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]

	def rand_Large_Land_Mass(self, i, j):
		if self.grid[i][j] != 'b':
			numb = self.get_Neighbour_Amount(i,j)

			roll = randint(1,6) + randint(1,6)

			if 1 <= roll <= 5:
				return [0.24,0.67,0.81]
			elif roll == 6 or roll == 7:
				return self.rand_Land_Picker()
			elif roll == 8:
				if numb <= 2:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 9:
				if numb <= 3:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 10:
				if numb <= 4:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 11:
				if numb <= 5:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 12:
				if numb <= 6:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]

	#Requires refinement.
	def rand_Large_Islands(self, i, j):
		if self.grid[i][j] != 'b':
			numb = self.get_Neighbour_Amount(i,j)

			roll = randint(1,6) + randint(1,6)

			if 1 <= roll <= 6:
				return [0.24,0.67,0.81]
			elif roll == 7:
				return self.rand_Land_Picker()
			elif roll == 8:
				if numb <= 2:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 9:
				if numb <= 3:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 10:
				if numb <= 4:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 11:
				if numb <= 5:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 12:
				if numb <= 6:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]

	def rand_Small_Islands(self, i, j):
		if self.grid[i][j] != 'b':
			numb = self.get_Neighbour_Amount(i,j)

			roll = randint(1,6) + randint(1,6)

			if 1 <= roll <= 7:
				return [0.24,0.67,0.81]
			elif roll == 8:
				return self.rand_Land_Picker()
			elif roll == 9:
				if numb <= 1:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 10:
				if numb <= 2:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 11:
				if numb <= 3:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]
			elif roll == 12:
				if numb <= 4:
					return self.rand_Land_Picker()
				else:
					return [0.24,0.67,0.81]

	
	def rand_Random(self):
		coords = [(x,y) for x in range(self.gridWidth) for y in range(self.gridHeight)]
		shuffle(coords)
		for i,j in coords:
			if self.grid[i][j] != 'b':
				self.grid[i][j].colour = self.rand_Land_Picker()			

	def get_Neighbour_Amount(self, col, row):
		neighbours_Num = 0
		try:
			if self.grid[col][row] != 'b':
				neigh = self.grid[col][row].get_Neighbours(0)
				if self.grid[neigh[0]][neigh[1]].colour != [0.24,0.67,0.81]:
					neighbours_Num += 1
		except Exception:
			pass
		try:
			if self.grid[col][row] != 'b':
				neigh = self.grid[col][row].get_Neighbours(1)
				if self.grid[neigh[0]][neigh[1]].colour != [0.24,0.67,0.81]:
					neighbours_Num += 1
		except Exception:
			pass
		try:
			if self.grid[col][row] != 'b':
				neigh = self.grid[col][row].get_Neighbours(5)
				if self.grid[neigh[0]][neigh[1]].colour != [0.24,0.67,0.81]:
					neighbours_Num += 1
		except Exception:
			pass


class CatanHex:
	
	def __init__(self, col, row):
		self.colour = [0,0,0]
		self.token = 0
		self.col = col
		self.row = row
		self.x = 0
		self.y = 0

	#directions: 0 = Right, 1 = Top Right, 2 = Top Left, 3 = Left, 4 = Bottom Left, 5 = Bottom Right
	def get_Neighbours(self, direction): 
		neighbors = [[ [+1,  0], [ 0, -1], [-1, -1],[-1,  0], [-1, +1], [ 0, +1] ],[ [+1,  0], [+1, -1], [ 0, -1],[-1,  0], [ 0, +1], [+1, +1] ]]
		parity = self.row & 1
		d = neighbors[parity][direction]
		return [self.col + d[0], self.row + d[1]]