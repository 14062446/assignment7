import numpy as np

#Arrays for Question 1
a1 = np.arange(1,16,1).reshape((3,5)).T
a2 = a1[:,1]
a3 = a1[1:4,0:3]

#Arrays for Question 2
b1 = np.arange(25).reshape(5,5).T
b2 = np.array([1., 5, 10, 15, 20])

#Random array for Question 3
c = np.random.rand(10,3)

#Functions return the arrays for Question 1, used just for testing purposes
def return_global_variables1():
    return a1 
def return_global_variables2():
    return a2  
def return_global_variables3():
    return a3   

#Prints the arrays for Question 1
def print_global_variables():
    print a1
    print a2
    print a3
    
#Generates 4th array from Question 1                        
def array_operations():
    numbers_in_range = []
    for element in a1.flat:
        if element>3 and element<11:
            numbers_in_range.append(element)
    print numbers_in_range
    return numbers_in_range
    
#Generates final array for Question 2, accounts for error of dividing array element by 0.     
def element_wise():
    np.seterr(divide = 'raise')
    try:
        b3 = np.divide(b1, b2)   
    except:
        print "Unexpected result;cannot divide array element by 0."
    else:
        print b3
        return b3    
        
        

#Helper function used to generate array in Question 3
def find_nearest(array,value):
    try: 
        idx = (np.abs(array-value)).argmin()
        return array[idx]
    except:
        raise ValueError
    

#Generates two lists for Question 3    
def operate_on_array(x):
    closest_number_list = []
    columns_list = []
    altered_array = abs(x - 0.5)
    for row in x:
        d = find_nearest(row, 0.5)
        closest_number_list.append(d)
        indexes = np.argsort(altered_array)
    columns_list = indexes[:,0]    
    print closest_number_list 
    return closest_number_list
   