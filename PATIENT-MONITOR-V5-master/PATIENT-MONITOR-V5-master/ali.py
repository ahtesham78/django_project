# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a push button
		button = QPushButton("Mi", self)

		# setting geometry of button
		button.setGeometry(20, 25, 150, 150)

		# adding action to a button
		button.clicked.connect(self.ahtesham)

	# action method
	def hi(self):

		# printing pressed
		print("pressed")

	def ahtesham(self):
		print("hi")
		self.hi()

		for i in range (2,13):
			self.hi()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
