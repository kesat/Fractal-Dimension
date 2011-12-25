# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 00:02:31 2011

@author: busker
"""

__author__ = "Kivanc Esat"
__copyright__ = ""
__credits__ = ["Kivanc Esat, Mehmet Ali Anıl"]
__license__ = ""
__version__ = "0.1.2"
__maintainer__ = "Kivanc Esat"
__email__ = "esat [at] itu.edu.tr"
__status__ = "Production"


import numpy as np
import matplotlib.pyplot as plt
#import Image
#from __future__ import division

def box_counter (image, box_size):
    """
    """
    image_size = len(image) 
    total_box_number = image_size / box_size
    reduced = np.zeros((total_box_number, total_box_number))
    
    for row in range(0,image_size,box_size):
       for col in range(0,image_size,box_size):
        
            sum_m = 0           
            
            for box_row in range(row,(box_size+row)):
                for box_col in range(col,(box_size+col)):

                    sum_m = sum_m + image[box_row, box_col]
  
            if sum_m >= (box_size**2) / 2:
                reduced_row = row/box_size
                reduced_col = col/box_size
                reduced[reduced_row, reduced_col] = 1

    reduced_box_number = np.sum(reduced)
    return reduced_box_number

def box_size_iterator (image):
    """ 
    """
    list_box_size =[4,8,16,32,64,128,512]
    #list_box_size = np.zeros((n-2))
    #for (li_ctr, li) in enumerate(range(2,n)):
      #  list_box_size[li_ctr] = 2**li
        
    list_box_number = np.zeros(len(list_box_size))

    for (box_size_ctr, box_size) in enumerate(list_box_size):
        list_box_number[box_size_ctr]  = box_counter(image, box_size)
    
    return list_box_number, list_box_size

def plot_size_number (image):
    """
    """
    list_of_all = box_size_iterator(image)
    list_box_number = list_of_all[0]
    list_box_size = list_of_all[1]
   
    slope = np.polyfit(np.log(list_box_size),np.log(list_box_number),1)
    print slope
    #plt.loglog(list_box_size,list_box_number)
    #plt.xlabel('Box number'); plt.ylabel('Box number')
    #plt.yscale('log'); plt.xscale('log')
    #plt.show()
        
    