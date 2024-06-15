import sys
from PyQt5 import QtWidgets,QtCore, uic 
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLCDNumber, QVBoxLayout, QLabel, QGridLayout, QFrame, QGraphicsView
# from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from random import randint
import numpy as np
from PyQt5.QtCore import QTimer,QTime,Qt
import pyqtgraph as pg
# import os
import db as mydatabase

class MyWindow:
    def __init__(self) -> None:
        self.win = uic.loadUi("ml.ui")

        self.label_hr = self.win.findChild(QLabel, 'label_14')
        print(self.label_hr)

        self.label_rr = self.win.findChild(QLabel, 'label_15')
        print(self.label_rr)

        self.label_te = self.win.findChild(QLabel, 'label_16')
        print(self.label_te)

        self.label_pr = self.win.findChild(QLabel, 'label_29')
        print(self.label_pr)

        self.label_sp = self.win.findChild(QLabel, 'label_32')
        print(self.label_sp)

        self.label_pi = self.win.findChild(QLabel, 'label_11')
        print(self.label_pi)

        self.label_sy = self.win.findChild(QLabel, 'label_12')
        print(self.label_sy)

        self.label_pu = self.win.findChild(QLabel, 'label_13')
        print(self.label_pu)

        self.frame = self.win.findChild(QFrame,'frame') #kl ki
        print(self.frame)

        self.frame_2 = self.win.findChild(QFrame,'frame_2')
        print(self.frame_2)


        self.frame_3 = self.win.findChild(QFrame,'frame_3')
        print(self.frame_3)

        self.graph = self.win.findChild(QGraphicsView, 'graphicsView')
        self.graph_2 = self.win.findChild(QGraphicsView, 'graphicsView_2')
        self.graph_3 = self.win.findChild(QGraphicsView, 'graphicsView_3')
        # ecg components
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground('black')
        self.plotWidget.setGeometry(0, 0, 789, 182)
        self.plotWidget.showGrid(x = True, y = True, alpha = 1)
        self.plotWidget.setParent(self.graph)
        self.plotWidget.clear()


        # Timmer 1 for Updating The Paramete
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_data_random)
        self.num = 0
        self.timer.start(1000)
        print("Timmer 1 Started")


        # Timmer 2 for Updating The Paramete
        self.timer_2 = QTimer()
        self.timer_2.setInterval(1000)
        self.timer_2.timeout.connect(self.update_graph_data)
        self.num = 2
        self.timer_2.start(10)
        print("Timmer 2 Started")

        # Timmer 3 for Updating The Paramete
        self.timer_3 = QTimer()
        self.timer_3.setInterval(1000)
        self.timer_3.timeout.connect(self.update_graph_data1)
        self.num = 3
        self.timer_3.start(10)
        print("Timmer 3 Started")


    # def update_data(self):
    #     self.mydb = mydatabase.MyDB("settings.db")
    #     self.label_hr.setText(f"{self.mydb.get_setting('Hr')}")
    #     self.label_rr.setText(f"{self.mydb.get_setting('RR')}")
    #     self.label_te.setText(f"{self.mydb.get_setting('Tem')}")
    #     self.label_pr.setText(f"{self.mydb.get_setting('PR')}")
    #     self.label_sp.setText(f"{self.mydb.get_setting('SPO2')}")
    #     self.label_pi.setText(f"{self.mydb.get_setting('pid')}")
    #     bp = f"{randint(100, 150)}/{randint(100, 123)}"
    #     self.label_sy.setText(f"{bp}")
    #     self.label_pu.setText(f"({self.mydb.get_setting('Pluse')})")
    #     self.mydb.close_connection()

    def update_data_random(self):
        self.label_hr.setText(f"{randint(100, 150)}")
        self.label_rr.setText(f"{randint(100, 150)}")
        self.label_te.setText(f"{randint(100, 150)}")
        self.label_pr.setText(f"{randint(100, 150)}")
        self.label_sp.setText(f"{randint(100, 150)}")
        self.label_pi.setText(f"{randint(100, 1501111111)}")
        bp = f"{randint(100, 150)}/{randint(100, 123)}"
        self.label_sy.setText(f"{bp}")
        self.label_pu.setText(f"({randint(100, 150)})")


    def update_graph_data(self):
        self.plotWidget.clear()
        data = np.random.random(1000)
        # self.graph.plotItem.plot(data)
        self.plotWidget.plot(data)
        

    
    def update_graph_data1(self):
        self.plotWidget.clear()
        data = np.random.random(1000)
        # self.graph.plotItem.plot(data)
        self.plotWidget.plot(data)
        
        

    
    def show(self):
        self.win.show()
        print("mohd")
        print("mohd")



    # def window(self):
    #     self.num = 0
    #     self.graph = pg.PlotWidget()
    #     self.grid = QGridLayout()
    #     self.timer = QTimer()
    #     self.grid.addWidget(self.graph, 0, 0)
    #     self.setLayout(self.grid)
    #     self.timer.timeout.connect(self.update)
    #     self.timer.start(1000)
    #     self.graph.show()
    #     self.show()


    
    # def update(self):
    #     self.graph.plotItem.clear()
    #     data = np.random.random(100)
    #     self.graph.plotItem.plot(data)


app = QtWidgets.QApplication([])
win = MyWindow()
# win = uic.loadUi("cli.ui")
win.show()
sys.exit(app.exec())