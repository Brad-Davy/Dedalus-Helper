#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:45:26 2021

@author: bradleydavy
"""
import numpy as np
from DedalusHelper.helper_2D import Data as Data2D
import sys,os
import matplotlib.pyplot as plt
import h5py
from vtk.util import numpy_support
import vtk
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
        
class plotting:

    def __init__(self):
        pass
        
    def vector_plot(self, temperature, u, v, w, time_step,aspect_ratio):
    
        " Makes a 3d plot of the the field, surface top and bottom. "
          
        max_u = np.amax(u)
        u = u[time_step]
        v = v[time_step]
        w = w[time_step]
        t = temperature[time_step]
        
        
        
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        # Make the grid
        x, y, z = np.meshgrid(np.linspace(0, 2*np.pi,32),
                              np.linspace(0, 2*np.pi,32),
                              np.linspace(0, 1, 16))
        
        ax.set_box_aspect(aspect_ratio)
        
        
        def cstm_autumn_r(x):
            return plt.cm.coolwarm((np.clip(x,2,10)-2)/8.)
        
        def color_quiver_plot(scale,sparcity):
            for i in range(0,np.shape(u)[0],16):
                i=16
                for j in range(0,np.shape(u)[1]):
                    for k in range(0,np.shape(u)[2]):
                            #length = np.sqrt(u[i,j,k]**2 + v[i,j,k]**2 + w[i,j,k]**2)
                            length = t[i,j,k]
                            ax.quiver(x[i,j,k], y[i,j,k], z[i,j,k], u[i,j,k]/(scale*max_u), v[i,j,k]/(scale*np.amax(v)),
                                      w[i,j,k]/(scale*np.amax(w)), color = cstm_autumn_r(length*100),linewidth = 1)
        
        plt.contourf(x[:,:,-1],y[:,:,-1],1 + t[:,:,-1],100,cmap = 'coolwarm', alpha =0.2)
        plt.contourf(x[:,:,0],y[:,:,0],t[:,:,0],100, cmap = 'coolwarm', alpha = 1)
        color_quiver_plot(4,4)
            
            
                
    def plotly_plot(self, temperature, u, v, w, time_step,aspect_ratio):
    
    
        import plotly.graph_objects as go
        
        x, y, z = np.meshgrid(np.linspace(0, 2*np.pi,32),
                      np.linspace(0, 2*np.pi,32),
                      np.linspace(0, 1, 16))
                      
        
                      
        u = u[time_step]
        v = v[time_step]
        w = w[time_step]*10
        t = temperature[time_step]
        scene = dict(aspectratio=dict(x=1, y=1, z=1/(2*np.pi)))
        fig = go.Figure(
            data = go.Cone(x = x.reshape(-1),y = y.reshape(-1), z = z.reshape(-1), u = u.reshape(-1), v = v.reshape(-1), w = w.reshape(-1), cmin = 0, cmax = 300, showscale = False, sizeref=3,colorscale='thermal', color = t.reshape(-1)),
            
            layout = go.Layout(
                width = 1920,
                height = 1000,
                scene = scene,))

        fig.write_html('first_figure.html', auto_open=True)
                
    
