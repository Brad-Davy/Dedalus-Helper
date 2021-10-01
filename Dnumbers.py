import numpy as np
import h5py

## All classes in this module require that the appropriate subsitutions are made when running the simmulations ##
class Nusselt:
    
    " A class when given the Nusselt number data over time calculates the Nusselt number. "
    NUMBER = 0
    time_series = []
    
    def __init__(self):
        self.NUMBER = 0
        self.time_series = []
        pass
        
        
    def load_data(self,file_path):
    
        from dedalus.tools import post

        with h5py.File(str(file_path), mode='r') as file:
        
            data = np.copy(file['tasks']['Nusselt']) # Load datasets
        return data
    
        

    def determine_time_series(self,file_path):
    
        " Nusselt number is given by "
        
        nusselt = self.load_data(file_path)

        for lines in nusselt:
                self.time_series.append(np.average(lines))

    def determine_NUMBER(self,file_path):
    
        " Nusselt number is given by "
        
        self.determine_time_series(file_path) # updates the time series array
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
    
    def __init__(self):
        self.NUMBER = 0
        self.time_series = []
        pass
        
        
    def load_data(self,file_path):
    
        from dedalus.tools import post

        with h5py.File(file_path, mode='r') as file:
            # Load datasets
            u = np.copy(file['tasks']['u'])
            w = np.copy(file['tasks']['w'])
        return u, w
        
        
    def return_peclet(self,u,w):
    
        " Returns a peclet number for a given time step. "
        if len(np.shape(u)) == 2:
            summation = (u**2 + w**2)**0.5
        else:
            raise('Array should be of the form 2D.')

        return np.average(summation)
    

    def determine_time_series(self,file_path):
    
        u,w = self.load_data(file_path)
        
        for index in range(np.shape(u)[0]):
            p = self.return_peclet(u[index],w[index])
            self.time_series.append(p)
        return self.time_series

    def get_NUMBER(self):
    
        " getter for NUMBER "
        return self.NUMBER
    
        
    def get_time_series(self):
    
        " getter for time_series "
        return self.time_series
        
