import numpy as np
import matplotlib.pyplot as plt
import os

class Data:
    
    " Class to deal with the outputs of the Dedalus scripts, exclusivley in 1D "
    
    def __init__(self, data) -> 'Init':
        self.data = data
 
    
    def return_absolute(self,array) -> 'List':
        
        " Returns the absolute value of the list. "
        
        temporary_array = []
        
        for lines in array:
            temporary_array.append(abs(lines))
        
        return temporary_array
    
    
    def plot_in_a_plot(self,data_1,data_2,data_3, file_path, labels = {}, no_of_terms: int = 4):
    
        " Plots a series of lines and then a sub plot zoomed in. "
        if no_of_terms == 4:
            plt.rcParams['font.family'] = 'Serif'
            plt.rcParams['font.size'] = 18
            plt.rcParams['axes.linewidth'] = 2
            fig = plt.figure(figsize = (12,6))
            #plt.ylim(-0.015,0.015)
            plt.xlabel('Time', fontsize = 24)
            plt.ylabel('Average Magnitude', fontsize = 24)
            time = np.linspace(0,200,len(self.data))
            plt.plot(time, self.data, label = labels["data"])
            plt.plot(time, data_1, label = labels["data_1"])
            plt.plot(time, data_2, label = labels["data_2"])
            plt.plot(time, data_3, label = labels["data_3"])
            plt.plot(time,np.zeros(len(time)),'k--')
            plt.legend(fontsize = 28)
            a = plt.axes([.37, .55, .2, .2])
            plt.xticks([])
            #plt.yticks([])
            a.plot(time[-20:],self.data[-20:])
            a.plot(time[-20:],data_1[-20:])
            a.plot(time[-20:],data_2[-20:])
            a.plot(time[-20:],data_3[-20:])
            a.plot(time[-20:],np.zeros(20),'k--')
            plt.savefig(file_path)
            
        elif no_of_terms == 3:
            plt.rcParams['font.family'] = 'Serif'
            plt.rcParams['font.size'] = 18
            plt.rcParams['axes.linewidth'] = 2
            fig = plt.figure(figsize = (12,6))
            plt.xlabel('Time', fontsize = 24)
            plt.ylabel('Average Magnitude', fontsize = 24)
            #plt.ylim(-0.015,0.015)
            time = np.linspace(0,200,len(self.data))
            plt.plot(time, self.data, label = labels["data"])
            plt.plot(time, data_1, label = labels["data_1"])
            plt.plot(time, data_3, label = labels["data_3"])
            plt.plot(time,np.zeros(len(time)),'k--')
            plt.legend(fontsize = 28)
            plt.plot([time[-20],146],[self.data[-20],-7.1e-3],'k--')
            plt.plot([time[-1],202],[self.data[-1],-7.1e-3],'k--')
            a = plt.axes([.67, .15, .2, .2])
            plt.xticks([])
            #plt.yticks([])
            a.plot(time[-20:],self.data[-20:])
            a.plot(time[-20:],data_1[-20:])
            a.plot(time[-20:],data_2[-20:])
            a.plot(time[-20:],data_3[-20:])
            a.plot(time[-20:],np.zeros(20),'k--')
            plt.savefig(file_path)
        
    def plot_forces(self,data_1,data_2,data_3, file_path, labels = {}, no_of_terms: int = 4):
    
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 18
        plt.rcParams['axes.linewidth'] = 2
        fig = plt.figure(figsize = (14,14))
        plt.xlabel('Time', fontsize = 24)
        plt.ylabel('Average Magnitude', fontsize = 24)
    
        " Plots a series of lines and then a sub plot zoomed in. "
        if no_of_terms == 4:

            #plt.ylim(-0.015,0.015)
            time = np.linspace(0,200,len(self.data))
            plt.plot(time, self.data, label = labels["data"])
            plt.plot(time, data_1, label = labels["data_1"])
            plt.plot(time, data_2, label = labels["data_2"])
            plt.plot(time, data_3, label = labels["data_3"])
            plt.legend(fontsize = 20)
            plt.savefig(file_path)
            
        elif no_of_terms == 3:
            time = np.linspace(0,200,len(self.data))
            plt.plot(time, self.data, label = labels["data"])
            plt.plot(time, data_1, label = labels["data_1"])
            plt.plot(time, data_3, label = labels["data_3"])
            plt.legend(fontsize = 20)
            plt.savefig(file_path)
        
    def  return_data(self) -> '1D data':
        return self.data

    def plot_data(self) -> 'Matplotlib plot':
    
        ' Makes a matplotlib plot of the data'
    
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 18
        plt.rcParams['axes.linewidth'] = 2
        plt.plot(self.data, 'k--')
        plt.show()

    
    def run_fucntion(func):
    
        ' Runs the function with the added print arguments, practicing using decorators '
        def wrapper(*args, **kwargs):
            print('Running function {fucntion}.'.format(fucntion = func))
            func(*args, **kwargs)
            print('Functions has been ran.')
        return wrapper
        
        
    @run_fucntion
    def print_data(self):
        
        ' Prints the data to the console '
        print(self.data)
            


    def plot_time_series(self):
    
        ' Plots the time series of 1D data'
    
        if len(np.shape(self.data)) > 1:
        
            for lines in self.data:
                plt.figure(1)
                plt.cla() # these two lines clear the previous graph, so don't plot over top.
                plt.clf()
                plt.plot(lines, 'k--', label = self.name)
                plt.show()
            
        else:
            raise CustomError('Data is of the wrong format, should be a 2d array. The data given here is of the shape {shape}.'.format(shape = np.shape(self.data)))
            
            
    def compare_time_series(self, second_data, second_name):
    
        ' Plots a time series of the class data and a second data set. '
    
        if len(np.shape(self.data)) > 1:
        
            for i in range(len(self.data)):
                plt.plot(self.data[i], 'r--', label = self.name)
                plt.plot(second_data[i], 'b', label = second_name)
                plt.legend()
                plt.show()
            
        else:
            raise CustomError('Data is of the wrong format, should be a 2d array. The data given here is of the shape {shape}.'.format(shape = np.shape(self.data)))
            
            

    def save_to_txt(self, file_path: str) -> 'Numpy array':
        
        " Saves the data to a text file "
        
        with open(file_path,'a') as file:
            file.truncate(0) ## clears the file contents if there is any ##
            for lines in self.data:
                file.write(str(lines)+'\n')
            file.close()
        print('The file is saved in directory {directory}'.format(directory = file_path))
        return file_path
                
            
            
            
    def convert_to_np(self, file_path: str) -> 'Text file':

        " Convert txt data to numpy array to be plotted e.c.t "
        
        array = [] # temporary array to save too
        
        file = open(file_path,'r').read().split('\n')
        for lines in file:
            try:
                array.append(float(lines))
            except:
                print('Tried to append {data} to the array. '.format(data = lines))
        return array

            
            
    def compute_derivative(self,dx = 1):
    
    
        derivative = np.zeros(len(self.data))
        for i in range(1,len(self.data)):
                derivative[i] = (self.data[i] - self.data[i-1])/dx
            
        return derivative
        
        
        
class CustomError(Exception):

    ' Class which allows for custome exceptions '

    pass
