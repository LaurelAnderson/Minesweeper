import random

class mine_model: 
	def __init__(self): 
	
		#make a new game at the start
		self.newGame()
	
	def newGame(self):
	
		#start counting moves
		self.moveCount = 0
		
		#set bombs
		self.c = 10
		self.r = 10
		
		#make a grid that has rep of bombs
		self.grid1 = [[0] * (self.c+2) for i in range (self.r+2)]
		#set up a grid for ajacency
		self.grid2 = [[0] * (self.c+2) for i in range (self.r+2)]
		
		#1 and * for bomb
		for i in range(10):
			while(1):
				x,y = random.randint(0,9), random.randint(0,9)
				if self.grid1[x+1][y+1] != 1:
					self.grid1[x+1][y+1] = 1
					self.grid2[x+1][y+1] = "*"
					break
		#find adjacent numbers
		self.adjacent()
		
	#calculate the adjacency
	def adjacent(self):
		for j in range(1, self.r+1):
			for i in range(1, self.c+1):
				temp = 0
				if self.grid2[i][j] != "*":
					#diaganol
					temp += self.grid1[i-1][j-1]
					temp += self.grid1[i+1][j+1]
					temp += self.grid1[i-1][j+1]
					temp += self.grid1[i+1][j-1]
					#horiz/vert
					temp += self.grid1[i-1][j]
					temp += self.grid1[i+1][j]
					temp += self.grid1[i][j+1]
					temp += self.grid1[i][j-1]
					self.grid2[i][j] = temp			
		
	#connect the squares to the grid
	def getPressed(self, row, col):
		self.clicked = self.grid2[row+1][col+1]
		return self.clicked
		
	#return the move count	
	def getMoves(self):
		self.moveCount += 1
		return self.moveCount
	
	#keeps track of the game state
	def getState(self):
		# -1 -- loss
		# 0 -- in progress
		# 1 -- win
		
		#if we have pushed a bomb, we lose
		if self.clicked == '*':
			return -1
		#check the count if we are still playing
		elif self.moveCount < 90:
			return 0
		#if you mave moved 90 times you have won
		elif self.moveCount == 90:
			return 1
	
	
	
	
	
	
	
	
	
	
