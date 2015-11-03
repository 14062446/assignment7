import numpy as np 
from Array import *
from Mandelbrot import generate_fractal

    
def main():    
    print "Question 1 answers:"
    print_global_variables()
    array_operations()
    print "\nQuestion 2 answer:"
    element_wise()
    print "\nQuestion 3 answers:"
    operate_on_array(np.random.rand(10,3))    
    print "\nQuestion 4 answer:"
    generate_fractal()
   
if __name__ == "__main__":
     main()   
    