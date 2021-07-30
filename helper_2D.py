import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

class IO:
    
    "Class which deals with the input and output of raw data, writing/reading them to text files e.c.t"
    
    def __init__(self):
        
        " Initiates the class, name is a dummy variable. "
        pass
        

    
    def test_float(self, datum: float,suppress_print: bool = True) -> 'bollean':
        
        " Tests if the data passed in is a float. "
        
        try:
            float(datum)
            return True
        except:
            data_type = type(datum)
            if suppress_print == False:
                print('Not a float Value, data type set to: {typ} and is of the form {dat}.'.format(typ = data_type,dat = datum))
            else:
                pass
            return False
            
        
            
    def convert_txt_np(self,file_path: str) -> 'numpy array':
        
        " Converts a txt file to a numpy array to plot with. "
        
        index = 0
        one_data = []
        two_data = []
        data  = open(file_path,'r').read().split('\n')
        for lines in data:
            for numbers in lines.split(','):
                
                if self.test_float(numbers) == True:
                    one_data.append(float(numbers))       

            two_data.append(one_data)
            one_data = []
        del(two_data[-1])
        return two_data
    
    
    def check_file(func) -> 'Checks the file exists':
        
        def wrapper(*args,**kwargs):
        
            if os.path.exists(kwargs.get('file_path')):
                func(*args, **kwargs)
            else:
                os.system('mkdir ' + os.path.dirname(kwargs.get('file_path')))
                func(*args, **kwargs)
        return wrapper
    
    
    @check_file
    def convert_np_txt(self, array: list, file_path: str) -> 'text file':
        
        """ Should be a 2d numpy array which is written to a text file in a manner which can be easily read. """
        

        file = open(file_path,'a')
        file.truncate(0) ## clears the file contents if there is any ##
        for lines in array:
            for numbers in lines:
                file.write(str(numbers)+',')
            file.write('\n')
        
        print('The file is saved in directory {directory}'.format(directory = file_path))
        return file_path
        


class Data:
    
    " Class which deals with data in the form of 2d numpy arrays, i.e. a single time step of the solution "
    
    def __init__(self,data) -> 'init':
        
        self.data = data
        self.nusselt_number = 1



    def temperature_plot(self):
        
        " Creates a temperature plot using the imshow library. "
        
        self.data = np.rot90(self.data, k=1, axes=(0, 1))
        plt.imshow(self.data,cmap='coolwarm')
        plt.colorbar()
        plt.show()
        
    def save_temperature_plot(self, file_name: str) -> 'matplotlib figure':
        
        " Saves a nice image of the plot as .eps file which can be used in latex"
        
        fig = plt.figure(figsize = (5,5))
        self.data = np.rot90(self.data, k=1, axes=(0, 1))
        plt.imshow(self.data,cmap='coolwarm',interpolation = 'bicubic')
        plt.colorbar()
        plt.rcParams['font.family'] = 'Serif'
        plt.rcParams['font.size'] = 18
        plt.rcParams['axes.linewidth'] = 2
        fig.savefig(file_name)

    def plot_line(self,position: int, row: bool = True) -> 'list':
        
        " Plots a line of a given position accross the domain. "
        
        if row == True:
            plt.plot(self.data[position], color = 'black')
            plt.xlabel('X - Domain')
            plt.ylabel('Temperature')
            
            return self.data[position]
        
        else:
            array = []
            for lines in self.data:
                array.append(lines[position])
                
            plt.plot(array, color = 'black')
            plt.xlabel('X - Domain')
            plt.ylabel('Temperature')
            
            return array


    def get_average_temperature(self):
        return np.average(np.array(self.data))
    
    
    def get_heat_transfer(self):
        return np.average(self.data[0])


    def return_average(self):
    
        " Returns the average of a 2D array. "
    
        AVG = []
        for lines in self.data:
            AVG.append(np.average(lines))
        return np.average(AVG)


class RawData:
    
    " A class which deals with multiple timesteps, takes data in the form of the 3D array of 2D time steps. "
    
    def __init__(self, data):
        self.data = data
        
    def return_timestep(self, index):
        return self.data[index]
    
    
    def determine_average(self,line_data):
        plt.plot(line_data)
    
    def determine_heat_flux(self):
        
        " Function which returns the noussalt number of a given RB simulation "
        " Nousselt number is given by: Nu = hL/k_f"
        " h = convective heat transfer coefficient, L = charecteristic length, k_f = thermal conductivity "
        " Expects to get the dT/dz data at the boundary "
        
        temp_flux = []
        
        for lines in self.data:
            temp_flux.append(np.average(lines[0]))
            
        average = self.determine_average(temp_flux)
            
        return average 
    
    
class ForceBalance:
    
    def __init__(self, data) ->  'Init':
        self.data = data
    
    @staticmethod
    def _internal_method():
        " Cant access class atributes, `dosnt take any arguments"
    
    
    def run_function(func) -> 'Runs Fucntions':
        
        def wrapper(*args, **kwargs):
            print('Started')
            func(*args, **kwargs)
            print('Ended')
            
        return wrapper
    
    
    @run_function
    def _temperature_flux_plot(self, i: float) -> 'Line plot':
        
        ' Evaluates the temperature flux at the top and bottom boundary, the sum of which should be 0. '
        
        for lines in self.data:
            print(lines)







