import numpy as np
import matplotlib.pyplot as plt


class Data:
    
    " Class to deal with the outputs of the Dedalus scripts, exclusivley in 1D "
    
    def __init__(self, data, name: str) -> 'Init':
        self.data = data
        self.name = name
        
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
            
            
            
            
            
            
            
            
class CustomError(Exception):

    ' Class which allows for custome exceptions '

    pass
