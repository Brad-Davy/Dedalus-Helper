import numpy as np
import matplotlib.pyplot as plt
import os 


class IO:
    
    def __init__(self):
        
        " Initiates the class, name is a dummy variable. "
        pass
        

    
    def test_float(self,datum,suppress_print = True):
        
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
            
        
            
    def convert_txt_np(self,file_name):
        
        " Converts a txt file to a numpy array to plot with. "
        
        index = 0
        one_data = []
        two_data = []
        data  = open(file_name,'r').read().split('\n')
        for lines in data:
            for numbers in lines.split(','):
                
                if self.test_float(numbers) == True:
                    one_data.append(float(numbers))       

            two_data.append(one_data)
            one_data = []
        del(two_data[-1])
        return two_data
    
    
    def convert_np_txt(self, array, file_name):
        
        " Should be a 2d numpy array which is written to a text file in a manner which can be easily read. "
        
        file = open(file_name,'a')
        file.truncate(0) ## clears the file contents if there is any ##
        for lines in array:
            for numbers in lines:
                file.write(str(numbers)+',')
            file.write('\n')
            
        file_path = os.getcwd()+'/'+file_name
        print('The file is saved in directory {directory}'.format(directory = file_path))
        return file_path
              


class Data:
    
    def __init__(self,data):
        
        self.data = data
        self.nusselt_number = 1



    def temperature_plot(self):
        
        " Creates a temperature plot using the imshow library. "
        
        self.data = np.rot90(self.data, k=1, axes=(0, 1))
        plt.imshow(self.data,cmap='coolwarm')
        plt.colorbar()
        plt.show()


    def plot_line(self,position, row = True):
        
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
            

    def determine_nusselt_number(self):
        
        " Function which returns the noussalt number of a given RB simulation "
        " Nousselt number is given by: Nu = hL/k_f"
        " h = convective heat transfer coefficient, L = charecteristic length, k_f = thermal conductivity "
        
        np.average(np.average(self.data[0]))
        
        
        return nousselt_number  

        
    def get_nusselt_number(self):
        return self.nusselt_number


    def get_average_temperature(self):
        return np.average(np.array(self.data))
    
    
    def get_heat_transfer(self):
        
        
        return np.average(self.data[0])
























