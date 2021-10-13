import numpy as np
import matplotlib.pyplot as plt

def return_time_derivative(array_1, array_2, dt: float) -> 'Array of arrays':
    
    " Given 2 arrays a backwards difference approximation of the time derivative is returned "
    " Approximates du/dt = (u^n+1 - u^n-1) / 2*dt "
    " Repeats for all points in the domain and returns the average and an array of du/dt at each point"
    
    new_array = (array_1 - array_2) / (2*dt)
    time_derivative = np.average(new_array)
    return time_derivative, new_array


def append_run_file(file_path: str, message: str):

    file = open(file_path,'a')
    file.write(message+'\n')
    file.close()

def clear_run_file(file_path: str):

    file = open(file_path,'w')
    file.write('')
    file.close()

if __name__ == '__main__':
    pass

