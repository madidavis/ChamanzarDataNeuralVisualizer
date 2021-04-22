#***SETUP***#
#Import Graphics Libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from datetime import datetime

#Import Processing & Data Science Libraries
import numpy as np
import pandas as pd
import random
import sys, os
import scipy.signal as sig 

#Import Custom Libraries
from recorded_file_selector_window import *
from waveform_visualiser_window import *
from recorded_project_control_panel import *
from recorded_file_filtering import *



#*** SETUP MAIN WINDOW ***#
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Define Main Window QtWidgets
        self.setWindowTitle("Real Time Data Visualiser")
        self.window_width = self.frameGeometry().width()
        self.window_height = self.frameGeometry().height()

        #MAIN LAYOUT
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_container = QWidget()

        #PROJECT TOGGLE WINDOW
        self.current_file = None#current file loaded into the window

        #RECORDED FILE SELECTOR WINDOW
        self.file_selection_window = File_Selection_Window(self)
        self.main_layout.addWidget(self.file_selection_window.file_window_container, 0, 0)

        #WAVEFORM VIEWER WINDOW
        self.waveform_viewer_window = Waveform_Viewer_Window(self)
        self.waveform_viewer_main_window = Waveform_Viewer_Main_Window(self)
        self.main_layout.addWidget(self.waveform_viewer_main_window.viewer_window_container, 0, 1)

        #CONTROL PANEL WINDOW
        self.control_panel_window = Control_Panel_Window(self)
        self.main_layout.addWidget(self.control_panel_window.container, 0, 2)

        #FILTERING WIDGET WINDOW
        self.filtering_panel_window = Filter_Control_Panel_Window(self)
        self.main_layout.addWidget(self.filtering_panel_window.container, 1, 2)

        #SET AND SHOW LAYOUT
        self.main_container.setLayout(self.main_layout)
        self.setCentralWidget(self.main_container)

    #load new file into the visualiser window
    def load_new_recorded_file(self, f):
        self.current_file = f

        #set up waveform visualiser window
        self.waveform_viewer_main_window.load_new_recorded_file_visualiser(f)
        #setup control panel
        self.control_panel_window.load_new_file(f)
        self.filtering_panel_window.load_new_file(f)




#*** RUN APPLICATION ***#
#create an application
app = QApplication(sys.argv)

#create and show the main window
main = MainWindow()
main.show()

#start the event loop
app.exec_()
