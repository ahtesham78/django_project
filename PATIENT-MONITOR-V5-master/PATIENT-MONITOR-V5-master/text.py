import os
import sys
from PyQt5 import QtWidgets, uic 
from PyQt5.QtWidgets import  QPushButton, QLabel, QFrame, QGraphicsView, QLabel
# from PyQt5 import QtGui
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
from random import randint
import numpy as np
from PyQt5.QtCore import QTimer
# from PyQt5.QtCore import QTime,Qt
import pyqtgraph as pg
# import os
import db as mydatabase
# import sqlite3
from threading import Thread


class MyWindow:
    def __init__(self) -> None:
        super().__init__()
        self.win = uic.loadUi("ml.ui")

        # Label 14
        self.label_hr = self.win.findChild(QLabel, 'label_14')
        print(self.label_hr)
    
        # Label 15
        self.label_rr = self.win.findChild(QLabel, 'label_15')
        print(self.label_rr)

        # Label 16
        self.label_te = self.win.findChild(QLabel, 'label_16')
        print(self.label_te)
        
        # Label 29
        self.label_pr = self.win.findChild(QLabel, 'label_29')
        print(self.label_pr)
        
        # Label 32
        self.label_sp = self.win.findChild(QLabel, 'label_32')
        print(self.label_sp)
        
        # Label 11
        self.label_pi = self.win.findChild(QLabel, 'label_11')
        print(self.label_pi)

        # Label 12
        self.label_sy = self.win.findChild(QLabel, 'label_12')
        print(self.label_sy)
        
        # Label13
        self.label_pu = self.win.findChild(QLabel, 'label_13')
        print(self.label_pu)
<<<<<<< ahtesham
        
        # Frame 1
=======

>>>>>>> master
        self.frame = self.win.findChild(QFrame,'frame') 
        print(self.frame)
    
        # Frame 2
        self.frame_2_b = self.win.findChild(QFrame,'frame_2')
        print(self.frame_2_b)

        # Frame 3
        self.frame_3_c = self.win.findChild(QFrame,'frame_3')
        print(self.frame_3_c)

        # Graphics view

        self.graph = self.win.findChild(QGraphicsView, 'graphicsView')
        
        # Graphics view2
        self.graph_2 = self.win.findChild(QGraphicsView, 'graphicsView_2')
        
        # Graphics view3
        self.graph_3 = self.win.findChild(QGraphicsView, 'graphicsView_3')

        # Button For video Hs
        self.pushButton = self.win.findChild(QPushButton,'pushButton')
        self.pushButton.clicked.connect(self.Audio)

        # Button For video fs
        self.pushButton_2 = self.win.findChild(QPushButton,'pushButton_2')
        self.pushButton_2.clicked.connect(self.viedo)

        # Button For video Alarm on 
        self.pushButton_3 = self.win.findChild(QPushButton,'pushButton_3')
        self.pushButton_3.clicked.connect(self.clicked)

        # Button For PID
        self.pushButton_4 = self.win.findChild(QPushButton,'pushButton_4')
        # self.pushButton_4.clicked.connect(self.pid_new_window)
        self.pushButton_4.clicked.connect(lambda : Thread(target= lambda: os.system("python v2_main.py")).start())

        # Button For Upload Status
        self.pushButton_5 = self.win.findChild(QPushButton,'pushButton_5')
        self.pushButton_5.clicked.connect(self.uploadStatus)

        # Button For Battery
        self.pushButton_6 = self.win.findChild(QPushButton,'pushButton_6')
        self.pushButton_6.clicked.connect(self.battery)

        self.pushButton_7 = self.win.findChild(QPushButton,'pushButton_7')
        # self.pushButton_7.clicked.connect(self.bell)
        
        # Button For Glob
        self.pushButton_8 = self.win.findChild(QPushButton,'pushButton_8')
        self.pushButton_8.clicked.connect(self.glob)
        
        # Button For setting
        self.pushButton_9 = self.win.findChild(QPushButton,'pushButton_9')
        self.pushButton_9.clicked.connect(self.setting)
        
        # Button For box
        self.pushButton_10 = self.win.findChild(QPushButton,'pushButton_10')
        self.pushButton_10.clicked.connect(self.box)
        
        # Button For add
        self.pushButton_11 = self.win.findChild(QPushButton,'pushButton_11')
        self.pushButton_11.clicked.connect(self.add)

        # ecg components
        self.plotWidget_1 = pg.PlotWidget()
        self.plotWidget_1.setBackground('black')
        self.plotWidget_1.setGeometry(0, 0, 789, 182)
        self.plotWidget_1.showGrid(x = True, y = True, alpha = 1)
        self.plotWidget_1.setParent(self.graph)
        self.plotWidget_1.clear()


        self.plotWidget_2 = pg.PlotWidget()
        self.plotWidget_2.setBackground('black')
        self.plotWidget_2.setGeometry(0, 0, 789, 182)
        self.plotWidget_2.showGrid(x = True, y = True, alpha = 2)
        self.plotWidget_2.setParent(self.graph_2)
        self.plotWidget_2.clear()

        self.plotWidget_3 = pg.PlotWidget()
        self.plotWidget_3.setBackground('black')
        self.plotWidget_3.setGeometry(0, 0, 789, 182)
        self.plotWidget_3.showGrid(x = True, y = True, alpha = 3)
        self.plotWidget_3.setParent(self.graph_3)
        self.plotWidget_3.clear()


        # Timmer 1 for Updating The Paramete
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_data_random)
        self.num = 0
        self.timer.start(1000)
        print("Timmer 1 Started")


        # Timmer 2 for Updating The Paramete
        self.timer_2 = QTimer()
        self.timer_2.setInterval(50)
        self.timer_2.timeout.connect(self.update_graph_data)
        self.num = 2
        self.timer_2.start(10)
        print("Timmer 2 Started")


    def update_data(self):
        self.mydb = mydatabase.MyDB("settings.db")
        self.label_hr.setText(f"{self.mydb.get_setting('Hr')}")
        self.label_rr.setText(f"{self.mydb.get_setting('RR')}")
        self.label_te.setText(f"{self.mydb.get_setting('Tem')}")
        self.label_pr.setText(f"{self.mydb.get_setting('PR')}")
        self.label_sp.setText(f"{self.mydb.get_setting('SPO2')}")
        self.label_pi.setText(f"{self.mydb.get_setting('pid')}")
        bp = f"{randint(100, 150)}/{randint(100, 123)}"
        self.label_sy.setText(f"{bp}")
        self.label_pu.setText(f"({self.mydb.get_setting('Pluse')})")
        self.mydb.close_connection()

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
        data = np.random.random(1000)

        self.plotWidget_1.clear()
        self.plotWidget_2.clear()
        self.plotWidget_3.clear()
        
        self.plotWidget_1.plot(data)
        self.plotWidget_2.plot(data)
        self.plotWidget_3.plot(data)     
    
    def show(self):
        print("mohd")
        print("mohd")
        self.win.show()
        

    def Audio (self):
        print("Audio")

    def viedo (self):
        print("viedo")

    def clicked(self):
        print("Alarm on")    

    def uploadStatus(self): 
        print("uploadStatus")

    def battery(self):
        print("battery percentag")

    def bell(self):
        print("bell")

    def glob(self):
        print("glob")
    
    def setting(self):
        print("setting")

    def box(self):
        print("box")

    def add(self):
        print("add")

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())