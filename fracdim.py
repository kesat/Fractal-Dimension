# Fractal Dimension Calculator

__author__ = "Kivanc Esat"
__copyright__ = ""
__credits__ = ["Kivanc Esat, Mehmet Ali Anil"]
__license__ = ""
__version__ = "0.2.5"
__maintainer__ = "Kivanc Esat"
__email__ = "esat [at] itu.edu.tr"
__status__ = "Production"



import numpy as np
import matplotlib.pyplot as plt


def box_counter (image, box_size):
    """
    """
    image_size = len(image)   # ONLY WORKS WITH SQUARE IMAGE    
    total_box_number = (image_size / box_size) # ONLY WORKS WITH SQUARE IMAGE
    reduced = np.zeros((total_box_number, total_box_number)) # ONLY WORKS WITH SQUARE IMAGE
    print box_size
    for row in range(0,image_size,box_size)[:-1]:  # ONLY WORKS WITH SQUARE IMAGE
       for col in range(0,image_size,box_size)[:-1]: # ONLY WORKS WITH SQUARE IMAGE
         
            sum_m = 0    
            for box_row in range(row,(box_size+row)): 
                for box_col in range(col,(box_size+col)):  
                    
                    sum_m = sum_m + image[box_row, box_col]
            
            if sum_m >= 1 :#(box_size**2) / 2.0:
                reduced_row = row/box_size
                reduced_col = col/box_size
                reduced[reduced_row, reduced_col] = 1
   
    reduced_box_number = np.sum(reduced)  
    return reduced_box_number

def box_size_iterator (image):
    """ 
    """
    list_box_size = range(2,100,1)  
    list_box_number = np.zeros(len(list_box_size))

    for (box_size_ctr, box_size) in enumerate(list_box_size):
        list_box_number[box_size_ctr]  = box_counter(image, box_size)
    return list_box_number, list_box_size

def slope_finder (image):
    """
    Hausdorff dimension : Dh = log(N) / log(1/r)
     
    Minkowski - Bouligand dimension : Dmb = 2 +
    log(Area(N)) /log(1/r) , Area(N)= Box_area*box_number
    """
    list_of_all = box_size_iterator(image)
    list_box_number = list_of_all[0]
    list_box_size =list_of_all[1]
    list_box_size_inv = np.divide(1.0, list_of_all[1])
    list_box_area = np.multiply(list_box_number, np.multiply(list_box_size,list_box_size))
    print 'box number'
    print list_box_number    
    print 'box size'
    print list_box_size
    print 'box size^2'
    print np.multiply(list_box_size,list_box_size)
    print 'box area= box number*boxsize^2'
    print list_box_area
       
    # Hausdorff dimension
    slope_haus = np.polyfit(np.log10(list_box_size_inv), np.log10(list_box_number),1) 
    print 'haus'
    print slope_haus
    
    # Minkowski - Bouligand dimension
    slope_mink = 2+np.polyfit(np.log10(list_box_size_inv), np.log10(list_box_area),1) 
    print 'mink'
    print slope_mink     
    
    plt.subplot(121)
    plt.loglog(list_box_size_inv, list_box_number, 'r')
    plt.ylabel('Box number'); plt.xlabel('1 / Box size')
    plt.yscale('log'); plt.xscale('log')
        
    
    plt.subplot(122) 
    plt.loglog(list_box_size_inv, list_box_area, 'r')
    plt.ylabel('Box area'); plt.xlabel('1 / Box size')
    plt.yscale('log'); plt.xscale('log')
            
    plt.show()
    