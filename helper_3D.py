#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:45:26 2021

@author: bradleydavy
"""
import numpy as np
from DedalusHelper.helper_2D import Data as Data2D
import sys,os
#sys.path.append(os.getcwd()) Append the current working directory to path


class Data:
    
    def __init__(self,data):
        self.data = data


    def return_data(self):
    
        " Returns the data stored in the class object. "
    
        return self.data

    def plot_slice(self, index: int, slice_type = 'Top_view'):
        
        ## Extract the required Index ##
        
        if slice_type == 'Top_view':
            data = self.data[:,:,index]
        
        elif slice_type == 'side_view':
            data = self.data[index,:,:]
            
        else:
            print('Invalid slice_type, expected Top_view or side_view')
            return 0
        data = Data2D(data)
        data.temperature_plot()
        
