import numpy as np
import matplotlib.pyplot as plt

class helper_2d:

    " Should take spectral data as self.data "

    def __init__(self, data):
        self.data = data

        
    def get_data(self):
        return self.data
    
    def return_absolute(self):
    
        " Given complex numbers are given by (a + ib), this function returns (a^2 + b^2). Note these qare numpy arrays."
        
        return (self.data.real**2 + self.data.imag**2)**0.5
    
    def temperature_plot(self):
        
        plotting_data = self.return_absolute()
        plotting_data = np.rot90(plotting_data, k=1, axes=(0, 1))
        plt.imshow(plotting_data,cmap='coolwarm',interpolation = 'bicubic')
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 18
        plt.colorbar()
        plt.show()


    def average_over_z(self):
    
        " Averages over the z domain. "

        data = self.return_absolute()
        array = [np.average(lines) for lines in data]
        return array
       

        
        
    def average_over_x(self):
    
        " Averages over the x domain. "
        
        data = self.return_absolute()
        array = [np.average(lines) for lines in np.rot90(data, k=1, axes=(0, 1))] # List comprehension used in Python
        return array[::-1]
        

class helper_3d:

    " Should take spectral data as self.data "

    def __init__(self, data):
        self.data = data

        
    
    def get_data(self):
        return self.data
    
    def return_absolute(self):
    
        " Given complex numbers are given by (a + ib), this function returns (a^2 + b^2)"
        
        return (self.data.real**2 + self.data.imag**2)**0.5

    
    def temperature_plot(self):
        
        plotting_data = self.return_absolute()
        plotting_data = np.rot90(plotting_data, k=1, axes=(0, 1))
        plt.imshow(plotting_data,cmap='coolwarm',interpolation = 'bicubic')
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 18
        plt.colorbar()
        plt.show()


    def average_over_z(self):
    
        " Averages over the z domain. "
    
        data = self.return_absolute()
        array = []
       
        for lines in data:
            
            array.append(np.average(lines))
            
        return array
        
        
    def average_over_x(self):
    
        " Averages over the z domain. "
    
        data = self.return_absolute()
        data = np.rot90(data, k=1, axes=(0, 1))
        array = []
       
        for lines in data:
            
            array.append(np.average(lines))
            
        return array[::-1]
