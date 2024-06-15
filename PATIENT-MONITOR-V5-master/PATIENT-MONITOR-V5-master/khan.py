from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QPushButton,QGridLayout, QVBoxLayout
from PyQt5.QtGui import QFont
import numpy as np
import pyqtgraph as pg


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.graph = pg.PlotWidget()
        self.grid = QGridLayout()
        self.timer = QTimer()
        self.grid.addWidget(self.graph, 0, 0)
        self.setLayout(self.grid)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.graph.show()
        self.show()


    
    def update(self):
        self.graph.plotItem.clear()
        data = np.random.random(100)
        self.graph.plotItem.plot(data)

app=QApplication(['Auto Update'])

win = Window()

app.exec_()