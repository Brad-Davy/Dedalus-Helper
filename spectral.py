import numpy as np
import matplotlib.pyplot as plt




class spectral_helper:

    " Should take spectral data as self.data "

    def __init__(self, data):
        self.data = data

        
    
    def return_data(self):
        return self.data
    
    def return_real_components(self):
    
        " Convert the data to real data "
        
        return np.real(self.data)
            
        
    def temperature_plot(self):
        
        plotting_data = np.real(self.data)
        plotting_data = np.rot90(plotting_data, k=1, axes=(0, 1))
        plt.imshow(plotting_data,cmap='coolwarm',interpolation = 'bicubic')
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 18
        plt.colorbar()
        plt.show()
