#***SETUP***#
#Import Graphics Libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from datetime import datetime
from itertools import count
from load_intan_rhd_format import *

#Import Processing & Data Science Libraries
import numpy as np
import pandas as pd
import random
import sys, os


#CLASSES
#Array of Neural Data derived from file
class Neural_File_Data(object):
    def __init__(self, file_name, sampling_rate, recording_length):
        self.file_name = file_name
        self.data_array = self.rhd_to_numpy()
        self.sampling_rate = sampling_rate
        self.recording_length = recording_length #no of seconds in the recording

        #Array Properties and Dimensions
        self.data_length = self.data_array.shape[1] #no of samples recorded
        self.time_val = np.linspace(0,self.recording_length,
                                    self.sampling_rate*self.recording_length)

        #Data plotting and Visualisation properties
        self.curr_range = [0, 3000]
        self.visible_time_xdata = []
        self.incr = 3000
        #self.visible_ydata = []

        #Properties for "Real-time" timer
        self.actual_range = [0, 3000]
        self.real_time_xdata = []
        self.real_incr = 3000
        #self.real_ydata = []

        #Channel Properties
        self.no_channels = self.data_array.shape[0]
        if self.no_channels > 6: self.no_active_channels = 4
        else: self.no_active_channels = self.no_channels
        self.channel_array = self.init_data_channels() #list of channel objects

    #Read .rhd file and return a numpy array of amplitude data
    def rhd_to_numpy(self):
        rhd_dic = read_data(self.file_name) #read rhd file
        rhd_array = rhd_dic["amplifier_data"] #extract relevant data and put in np array
        print(rhd_array, rhd_array.shape)
        return rhd_array

    #Set up a list of Channel Objects for all channels in the recording
    def init_data_channels(self):
        channel_list = []
        for i in range(self.no_active_channels):
            channel = Neural_Data_Channel(self, self.sampling_rate, i)
            channel_list.append(channel)
        return np.array(channel_list)

    #PLOTTING / DATA UPDATE VARIABLES
    #UPDATING PLOTTING RANGES
    #update range of data displayed in visualiser
    def update_curr_range (self):
        #update range bounds
        self.curr_range[0] += self.incr
        self.curr_range[1] += self.incr

        #update time data/x axis
        self.visible_time_xdata = self.time_val[self.curr_range[0]:self.curr_range[1]]

        #update channel data / y axis for each channel
        for i in range(self.no_active_channels):
            self.channel_array[i].update_channel_data_range(self.curr_range[0],self.curr_range[1])

    #reverse update the range of data displayed in the visualiser
    def reverse_update_curr_range(self):
        #update range bounds
        self.curr_range[0] -= self.incr
        self.curr_range[1] -= self.incr

        #update time data/x axis
        self.visible_time_xdata = self.time_val[self.curr_range[0]:self.curr_range[1]]

        #update channel data / y axis for each channel
        for i in range(self.no_active_channels):
            self.channel_array[i].update_channel_data_range(self.curr_range[0],self.curr_range[1])

    #update range of real time/ hidden data
    def update_actual_range(self):
        #update range bounds
        self.actual_range[0] += self.real_incr
        self.actual_range[1] += self.real_incr

        #update time data/x axis
        self.real_time_xdata = self.time_val[self.actual_range[0]:self.actual_range[1]]

        #update channel data / y axis for each channel
        for i in range(self.no_active_channels):
            self.channel_array[i].update_real_channel_data_range(self.actual_range[0],
                                                                 self.actual_range[1])




#Neural data for information pertaining to single channels
class Neural_Data_Channel(object):
    def __init__(self, file_data, sampling_rate,
                 channel_id):
        self.file_data = file_data
        self.sampling_rate = sampling_rate
        self.channel_id = channel_id
        self.channel_data = np.array(self.file_data.data_array[self.channel_id])

        #Plotting and Visualisation Attributes
        self.visible_ydata = np.array([])
        self.actual_ydata = np.array([])

        #Visibility / Pinned Attributes

    #PLOTTING / DATA UPDATE VARIABLES
    #UPDATING PLOTTING RANGES
    #Update visible range of channel data
    def update_channel_data_range(self, min, max):
        self.visible_ydata = self.channel_data[min:max]

    #update actual range of channel data
    def update_real_channel_data_range(self, min, max):
        self.actual_ydata = self.channel_data[min:max]



#test
#name = "8_GLUTAMATE_30kHz Sampling Freq_191221_183536.rhd"
#data = Neural_File_Data(name, 30000, 60)
