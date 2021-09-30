import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os

class animation:
    
    def __init__(self, data, fig):
        self.data = data
        os.system('rm -r /opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/img')
        os.system('mkdir /opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/img')
    
        
        
    def create_images(self) -> 'Out Images':
    
        " Given the time dependent data this function saves them as images "

        counter = 0
        for lines in self.data:
            
            if counter < 10:
                file_path = '/opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/img/000{counter}.png'.format(counter = counter)
            elif 9 < counter < 100:
                file_path = '/opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/img/00{counter}.png'.format(counter = counter)
            else:
                file_path = '/opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/img/0{counter}.png'.format(counter = counter)
            fig.savefig(file_path, dpi = 600)
            counter = counter + 1
                
        
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
        filenames = sorted(glob.glob('/opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/img/*.png'))
        
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave('/opt/anaconda3/envs/dedalus/lib/python3.8/site-packages/DedalusHelper/video/animation.gif', images)
        
    def return_all_data(self):
        return self.data
        
        
