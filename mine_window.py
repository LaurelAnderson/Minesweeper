from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from mine_model import *

class mine_window(QMainWindow):

	def __init__(self):
		super(mine_window, self).__init__()

		#set window title
		self.setWindowTitle("Minesweeper")
		self.setWindowIcon(QIcon('mine.png'))
		
		#connect to the model here
		self.model = mine_model()
		
		widget = QWidget()
		self.setCentralWidget(widget)		
	
		#Create menu bar and go to make a new game
		file_action = QAction("New Game", self)
		file_action.triggered.connect(self.newGame)
		main_menu = self.menuBar()
		file_menu = main_menu.addMenu('&File')
		file_menu.addAction(file_action)
		
		#make a vertical layout
		self.layout = QVBoxLayout()
		widget.setLayout(self.layout)
		
		#make a horizontal layout
		self.layoutH = QHBoxLayout()
				
		#add the layouts
		self.layout.addLayout(self.layoutH)
		
		#make a list of the buttons
		self.buttons = []
		
		#grid layouts figure out what size they need to be
		grid = QGridLayout()
		for i in range(100):
			self.button = QPushButton()
			self.button.clicked.connect(self.buttonClicked)
			self.buttons.append(self.button)
			row = i // 10
			col = i % 10
			self.button.setProperty("row", row)
			self.button.setProperty("col", col)
			self.button.setMaximumSize(40,40)
			self.button.setMinimumSize(40,40)
			self.button.setStyleSheet('QPushButton {background-color: #cccecf;}')

	
			grid.addWidget(self.buttons[i], row, col)
			grid.setSpacing(0)

		self.layout.addLayout(grid)
		
		#make a label for number of bombs in the game 
		self.bombNum = QLabel("Bombs: 10")#connect to bomb count
		font = QFont("Helvetica", 15, QFont.Bold)
		self.bombNum.setFont(font)
		self.bombNum.setAlignment(Qt.AlignLeft)
		self.layoutH.addWidget(self.bombNum)
		
		#make a label for moves
		self.numMoves = QLabel("Moves: 0")#connect to move count
		self.numMoves.setFont(font)
		self.numMoves.setAlignment(Qt.AlignRight)
		self.layoutH.addWidget(self.numMoves)
		
		#label for the game state
		self.gameState = QLabel("")
		self.gameState.setFont(font)
		self.gameState.setAlignment(Qt.AlignCenter)
		self.layout.addWidget(self.gameState)
	
		#make a label for the timer
		
	def newGame(self): 
		print("Start a new game!")
		
		#unlook all the buttons
		for button in self.buttons:
			button.setEnabled(True)
			button.setText("")
			button.setStyleSheet('QPushButton {background-color: #cccecf;}')
			
		#reset the move count display
		self.numMoves.setText("Moves: 0")
		
		#reset game state
		self.gameState.setText("")
				
		#connect this to the game model
		self.model.newGame()	
		
	def buttonClicked(self): 
		#sender() tells us who caused the action to take place
		press = self.sender()
		c = press.property("col")
		r = press.property("row")
		
		#update moveCount
		count = self.model.getMoves()
		self.numMoves.setText("Moves: " + str(count))

		#only can click once until new game. 
		press.setEnabled(False)
		press.setStyleSheet('QPushButton {background-color: #FFFFFF;}')
		
		#tell the model about the click and store it in action
		action = self.model.getPressed(r, c)
		press.setText(str(action))
		
		#update the game state
		if self.model.getState() == 1:
			self.gameState.setText("You Win!!!")
		elif self.model.getState() == -1:
			self.gameState.setText("You lose!!!")
			self.lose()
		
	def lose(self):
		#unlock all the squares in buttons
		for button in self.buttons:
			r = button.property("row")
			c = button.property("col")
			action = self.model.getPressed(r,c)
			button.setEnabled(False)
			button.setText(str(action))
			button.setStyleSheet('QPushButton {background-color: #FFFFFF;}')
			
			
