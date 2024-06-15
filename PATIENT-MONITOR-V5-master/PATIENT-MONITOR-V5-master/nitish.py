from turtle import width
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGraphicsView, QSlider, QCheckBox
from PyQt5 import uic
import sys
import pyqtgraph as pg
# from ecg_analyze import *
from os import path
# from API import *
from threading import Thread
import numpy as np

import pandas as pd

UI_FILE_PATH = path.abspath(path.join(path.dirname(__file__), 'cli.ui'))
DATA_FOLDER = "filtered_data"


class ReadCsvFile:
    def __init__(self, file_path):
        self.file_path = file_path
        print("Reading file: ", file_path)
        self.df = pd.read_csv(self.file_path)
    
    def get_data(self):
        return self.df

    def get_lead(self, lead):
        return self.df[lead]

    def get_all_leads_names(self):
        return self.df.columns.values.tolist()


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cli.ui", self)
        self.cutoff_frequency = 100  # default value (Hz) Low Pass Filter
        self.l_cutoff_frequency = 0.4  # default value (Hz) High Pass Filter
        self.global_data_array = np.zeros(2000)
        self.ecg_class_ = ""
        self.qrs_index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Analysis Graph')

        # Finfing the graph widget
        # self.graph = self.findChild(QGraphicsView, 'graphicsView')

        # # ECG Component graph
        # self.ecg_component = self.findChild(QGraphicsView, 'graphicsView_2')

        # # Find the next button
        # self.next_btn = self.findChild(QPushButton, 'pushButton_2')
        # self.next_btn.clicked.connect(self.next_file)

        # # Find the file name label and lead name label
        # self.file_name_label = self.findChild(QLabel, 'label_14')
        # self.lead_name_label = self.findChild(QLabel, 'label_16')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())