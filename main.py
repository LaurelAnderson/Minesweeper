from PyQt5.QtWidgets import QApplication
from mine_window import *

app = QApplication([])
window = mine_window()
window.show()
app.exec_()	
