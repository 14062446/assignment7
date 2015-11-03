import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class Grid(int):
    
    #initializes the granularity for grid
    def __init__(self, int):
        self.granularity = int(int)
        self.input_valid = False 
        while not self.input_valid:
            if not (type(self.granularity) == int and self.granularity > 2):
                self.granularity = int(raw_input('Invalid input. Specify new positive interger gran: '))
            else:
                self.input_valid = True
       
    #sets up grif for Mandelbrot Fractal     
    def set_grid_values(self):  
        self.x = np.linspace(-2,1,self.granularity)
        self.y = np.linspace(-1.5,1.5,self.granularity)
        self.xx, self.yy = np.meshgrid(self.x,self.y)
        return self.xx,self.yy
        print self.xx
Grid(8)

        