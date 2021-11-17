import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os
from tqdm import tqdm
class animation:
    
    def __init__(self, data, file_path: str, z):
    
        self.data = data
        self.file_path = file_path
        self.z = z

        
    def create_images(self) -> 'Out Images':
    
        " Given the time dependent data this function saves them as images "

        counter = 0
        fig = plt.figure(figsize = (8,4))
        for lines in tqdm(self.data):

            lines = np.rot90(lines, k=3, axes=(0, 1))
            ax = fig.add_subplot(111)
            plt.rcParams['font.family'] = 'Serif'
            plt.rcParams['font.size'] = 18
            ax.set_aspect('equal')
            X,Y = np.meshgrid(np.linspace(0,2,np.shape(lines)[1]),self.z)
            plt.contourf(X, Y, lines, 40, cmap='bwr')
            plt.colorbar()
                
            if counter < 10:
                filepath = 'img/000{counter}.png'.format(counter = counter)
            elif 9 < counter < 100:
                filepath = 'img/00{counter}.png'.format(counter = counter)
            else:
                filepath = 'img/0{counter}.png'.format(counter = counter)
                
                
            fig.savefig(filepath, dpi = 600)
            counter = counter + 1
            plt.clf()
                
        
    def check_data(func):
    
        " Checks the data is of the right format. "
        
        def wrapper(*args, **kwargs):
            shape = np.shape(kwargs.get('new_data'))
            if len(shape) == 2:
                func(*args, **kwargs)
            else:
                print(" Data is of the wrong format and as such the function didnt run. ")
            
        return wrapper
            
        
    
    @check_data
    def add_data(self, new_data):
        
        " Adds some data/image to the aniomation "
        
        self.data.append(new_data)
    
    
    def create_animation(self) -> 'Out .gif':
    
        " Creates a gif from the images generated "
    
        import imageio
        import glob
        filenames = sorted(glob.glob('img/*.png'))
        print(filenames)
        images = []
        for filename in tqdm(filenames):
            images.append(imageio.imread(filename))
            
        imageio.mimsave('animation.gif', images)
        
    def return_all_data(self):
        return self.data
        
        
