import numpy as np
import h5py
from DedalusHelper.spectral import helper_2d

## All classes in this module require that the appropriate subsitutions are made when running the simmulations ##
class Nusselt:
    
    " A class when given the Nusselt number data over time calculates the Nusselt number. "
    NUMBER = 0
    time_series = []
    
    def __init__(self, file_path):
        self.NUMBER = 0
        self.time_series = []
        self.file_path = file_path
        
        
    def load_data(self):
    
        from dedalus.tools import post

        with h5py.File(self.file_path, mode='r') as file:
        
            data = np.copy(file['tasks']['Nusselt']) # Load datasets
        return data
    
        

    def determine_time_series(self):
    
        " Nusselt number is given by "
        
        nusselt = self.load_data()

        for lines in nusselt:
                self.time_series.append(np.average(lines))
                
        return self.time_series

    def determine_NUMBER(self):
    
        " Nusselt number is given by "
        
        self.determine_time_series() # updates the time series array
        print(self.time_series)
        self.NUMBER = np.average(self.time_series) # Sets the number variable

    def get_NUMBER(self):
    
        " getter for NUMBER"
        return self.NUMBER
    
        
    def get_time_series(self):
    
        " getter for NUMBER"
        return self.time_series
        
        
    def determine_derivative(self):
    
        derivative = []
        if len(self.time_series) > 1:
            for i in range(len(self.time_series)-1):
                derivative.append(self.time_series[i+1] - self.time_series[i])
        else:
            raise(" Make sure time series has been determied before running this function. ")
        return derivative

    def steady_state(self, threshold):
        
        derivative = self.determine_derivative()
        steady_array = []
        
        for lines in derivative:
            if abs(lines) < threshold:
                steady_array.append(self.time_series[derivative.index(lines)])
        return steady_array

## All classes in this module require that the appropriate subsitutions are made when running the simmulations ##
class Peclet:
    
    " A class when given the Nusselt number data over time calculates the Nusselt number. "
    NUMBER = 0
    time_series = []
    
    def __init__(self, file_path):
        self.NUMBER = 0
        self.time_series = []
        self.file_path = file_path
    
        
    def load_data(self):
    
        from dedalus.tools import post

        with h5py.File(self.file_path, mode='r') as file:
            # Load datasets
            u = np.copy(file['tasks']['u'])
            w = np.copy(file['tasks']['w'])
        return u, w
        
        
    def return_peclet(self,u,w):
        
        " Returns a peclet number for a given time step. "
        
   
        if len(np.shape(u)) == 2:
            return np.average((u**2 + w**2)**0.5)
        else:
            pass

    
    

    def determine_time_series(self):
    
        u,w = self.load_data()
        for index in range(np.shape(u)[0]):
            p = self.return_peclet(u[index],w[index])
            self.time_series.append(p)
        return np.array(self.time_series)

    def get_NUMBER(self):
    
        " getter for NUMBER "
        return self.NUMBER
    
        
    def get_time_series(self):
    
        " getter for time_series "
        return self.time_series
        


class KineticEnergy:

    NUMBER = 0
    time_series = []
    
    def __init__(self, file_path):
        self.NUMBER = 0
        self.time_series = []
        self.file_path = file_path
        
        
    def load_spectral_data(self):
        with h5py.File(self.file_path, mode='r') as file:
            ## Load data sets ##
            ke = np.copy(file['tasks']['Spectrum Kinetic Energy'])
            
        return ke
    
    def load_real_data(self):
        with h5py.File(self.file_path, mode='r') as file:
            ## Load data sets ##
            ke = np.copy(file['tasks']['Real Kinetic Energy'])
            
        return ke
    
    def average_over_time(self,mode):
        
        if mode == 's':
            data = self.load_spectral_data()
        elif mode == 'r':
            data = self.load_real_data()
        else:
            print("Choose either r for real or s for spectral.")
            return None
        array = np.zeros(np.shape(data)[1])
        
        for i in range(np.shape(data)[0]):
            kep = helper_2d(data[i,:,:]).average_over_z()
            array += kep
        return array/np.shape(data)[0]
        
        
    def sum_over_domain(self, mode):
    
        array = []
        
        if mode == 's':
            data = self.load_spectral_data()
            for lines in data:
                array.append(np.sum(helper_2d(lines).return_absolute()))
            
            return np.array(array)
        elif mode == 'r':
            data = self.load_real_data()
            for lines in data:
                array.append(np.sum(lines))
            
            return np.array(array)
        else:
            print("Choose either r for real or s for spectral.")
            return None
    
 
        
            
            

    
        
