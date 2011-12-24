# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 00:02:31 2011

@author: busker
"""

__author__ = "Kivanc Esat"
__copyright__ = ""
__credits__ = ["Kivanc Esat, Mehmet Ali Anıl"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Kivanc Esat"
__email__ = "esat [at] itu.edu.tr"
__status__ = "Production"


import numpy as np
import Image
#from __future__ import division

def box_counter (image, box_size):
    
    image_size = len(image) 
    total_box_number = image_size / box_size
    reduced = np.zeros((total_box_number, total_box_number))
#    print Image_matrix ; print Image_matrix_size
    
    for row in range(0,image_size,box_size):
       for col in range(0,image_size,box_size):
        
            sum_m = 0           
            
            for box_row in range(row,(box_size+row)):
                for box_col in range(col,(box_size+col)):

                    sum_m = sum_m + image[box_row, box_col]
             
            #print sum_m
            #print row, col
            #print (box_row, box_col)

            if sum_m >= (box_size**2) / 2:
                reduced_row = row/box_size
                reduced_col = col/box_size
                reduced[reduced_row, reduced_col] = 1

    reduced_box_number = np.sum(reduced)
    #print reduced
    #print np.shape(reduced)
    #print reduced_box_number
    return reduced_box_number

def fractal_dimension (image):
    #print(image)    
    list_box_size=[4, 8, 16, 32]
    list_box_number = np.zeros(len(list_box_size))
    for box_size in list_box_size:
        #print box_size
        #print box_size_ctr
        list_box_number  = box_counter(image, box_size)
    return list_box_number, list_box_size
    
        
        