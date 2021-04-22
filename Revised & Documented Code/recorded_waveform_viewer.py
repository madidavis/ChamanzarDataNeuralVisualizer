"""
@file        recorded_waveform_viewer.py
 
@brief       Widget to Display dynamic and Static Plots of Neural Data

@author      Madi Davis <madelind@andrew.cmu.edu> 
"""

"""! @brief file setup"""
# Import Graphics / GUI Libraries
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
from recorded_mode_data import *

#! @brief STATIC DISPLAY WINDOW & WIDGETS #
"""! @brief Widget allowing User to select Recorded Files and Folders for Visualisation"""
class Recorded_Static_Waveform_Window(QWidget):
    """!  @brief Initialiser for Static Waveform Visualiser
          @param[in] visualiser_window - main visualiser widget
          @return - instance of Recorded Waveform Window
    """
    def __init__(self, visualiser_window):
        super().__init__()
        #WINDOW & LAYOUT PROPERTIES
        self.visualiser_window = main_window
        self.container = QWidget() # main container
        self.layout = QVBoxLayout()

        #SETUP WINDOW LAYOUT
        self.container = QWidget()
        self.container.setLayout(self.layout)
    
    """! @brief load new file data into the static visualiser """
    def load_new_file



#! @brief MAIN DISPLAY WINDOW #
"""! @brief Widget to display visualisations of selected files"""
class Recorded_Waveform_Window(QWidget):
    """!  @brief Initialiser for Recorded Mode Waveform Visualisatin Window
          @param[in] recorded_window - main GUI window for recorded mode
          @param[in] recorded_data - data associated with recorded mode for current project
          @return - instance of Recorded Waveform Window
    """
    def __init__(self, recorded_window):
        super().__init__()

        # @brief WINDOW & LAYOUT PROPERTIES
        self.recorded_window = recorded_window;
        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.window_label = QLabel("Waveform Viewer")
        self.layout.addWidget(self.window_label)

        # @brief DATA PROPERTIES
        self.recorded_data = None

        #DYNAMIC WINDOW PROPERTIES

        #TAB PROPERTIES

        #SETUP WINDOW LAYOUT
        self.container = QWidget()
        self.container.setLayout(self.layout)
    
    '''! @brief load new Recorded Project data into file browser 
         @param[in] data - Recorded Mode Data object
    '''
    def load_recorded_project_data(self, data):
        self.recorded_data = data


