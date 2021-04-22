"""
@file        visualiser_project.py
 
@brief       Stores Data Associated with a specific project 

@author      Madi Davis <madelind@andrew.cmu.edu> 
"""

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

"""! @brief Defines class project instances"""
class Visualiser_Project():
    """!  @brief Initialiser for Recorded Mode Data
          @param[in] name - parent project
          @return - instance of Project Object
    """
    def __init__(self, name):
        self.name = name
        self.recorded_mode_data = Recorded_Mode_Data(self)
        self.real_time_mode_data = None
    
