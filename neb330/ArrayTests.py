from Array import *
import numpy as np  
import unittest 

    
array_1 = [[1,  6, 11], [2,  7, 12], [3,  8, 13], [4,  9, 14], [5, 10, 15]] 
   
array_2 = [6, 7, 8, 9, 10]

array_3 = [[2, 7, 12],[ 3, 8, 13],[ 4, 9, 14]]

array_4 = [6, 7, 8, 4, 9, 5, 10]
    
array_5 = [[ 0.        ,  1.        ,  1.        ,  1.        ,  1.        ],
       [ 1.        ,  1.2       ,  1.1       ,  1.06666667,  1.05      ],
       [ 2.        ,  1.4       ,  1.2       ,  1.13333333,  1.1       ],
       [ 3.        ,  1.6       ,  1.3       ,  1.2       ,  1.15      ],
       [ 4.        ,  1.8       ,  1.4       ,  1.26666667,  1.2       ]]


class ArrayTests(unittest.TestCase):
    
    def test_array_values(self):
        np.testing.assert_array_equal( return_global_variables1(), array_1)
        np.testing.assert_array_equal( return_global_variables2(), array_2)
        np.testing.assert_array_equal( return_global_variables3(), array_3)
    
    def test_array_operations(self):
        np.testing.assert_array_equal( array_operations(), array_4)     
     
    def test_element_wise(self):
        np.testing.assert_array_almost_equal( element_wise(), array_5) 
       
        

            
        