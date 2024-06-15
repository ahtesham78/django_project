from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QPushButton,QToolTip,QMessageBox,QAction,QLineEdit,QToolButton,QMainWindow,QCheckBox,QLabel, QRadioButton,QVBoxLayout
from db import *
import sqlite3


mydb = MyDB("settings.db")
print(mydb.get_setting("record"))

def printt():
    v2=win.lineEdit_2.text()
    v3=win.lineEdit_3.text()
    v4=win.lineEdit_4.text()
    v5=win.lineEdit_5.text()
    v=win.lineEdit.text()
    v6=win.lineEdit_6.text()
    v7=win.lineEdit_7.text()
    v8=win.lineEdit_8.text()
    v9=win.lineEdit_9.text()
    r1=win.radioButton("Male")
    r2=win.radioButton("female")

    print("mohd")
    print("abbas")
    print("Enter your Name ! ! :",v2)
    print("You your Dob! ! :",v3)
    print("You your Age ! ! :",v4)
    print("You your Height ! ! :",v5)
    print("You your weight ! ! :",v)
    print("YouBloodPressure ! ! :",v6)
    print("You Medication  ! ! :",v7)
    print("You Date  ! ! :",v8)
    print("Enter your Pid  ! ! :",v9)
    print("You Gender is ! ! :",  r1)
    print("You Gender is ! ! :",  r2)
    print("==================")
    
    mydb.update_setting("bp",v6)
    mydb.update_setting("medication",v7)
    mydb.update_setting("date",v8)
    mydb.update_setting("name",v2)
    mydb.update_setting("pid",v9)
    mydb.update_setting("age",v4)
    mydb.update_setting("gender",)
    mydb.update_setting("Height",v5)
    mydb.update_setting("Dob",v3)
    mydb.update_setting("weight",v)   
    print("Record inserted")
    win.close()


def exit_window():
        win.close()


def clearLayout(layout):
      win.lineEdit_2.clear()
      win.lineEdit_3.clear()
      win.lineEdit_4.clear()
      win.lineEdit_5.clear()
      win.lineEdit.clear()
      win.lineEdit_7.clear()
      win.lineEdit_8.clear()
      win.lineEdit_6.clear() 
    #   win.lineEdit_9.clear()


app = QtWidgets.QApplication([])
win = uic.loadUi("pid_widget.ui") #specify the location of your .ui file
win.pushButton_2.clicked.connect(printt)
win.pushButton_3.clicked.connect(exit_window)
win.pushButton.clicked.connect(clearLayout)


win.show()
sys.exit(app.exec())

