# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:11:44 2011
44
@author: busker
"""

import numpy as np
import fracdim as fr
import Image

#image = np.ones((512,512))
#image =  pl.Image.open('/home/busker/Documents/Fractal-Dimention/Test_images/Norway_municipalities_fdim-1.52__treshold_512-512.png')


#fr.slope_finder(image)

def image_converter (image_pattern):
    image = Image.open(image_pattern)
    image_binary = image.convert('1')
    image_binary_list= list(image_binary.getdata())
    image_binary_matrix = (np.resize(image_binary_list, image_binary.size)!=255)*1 #thanks to mali
    
    return image_binary_matrix

image = image_converter ('Test_images/Sierpinski_gasket.png')
slope =  fr.slope_finder(image)

print slope
    