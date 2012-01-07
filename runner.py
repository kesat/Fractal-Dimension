# Runner for fracdim module


import numpy as np
import fracdim as fr
import Image

def image_converter (image_pattern):
    '''
    '''
    image = Image.open(image_pattern)
    image_binary = image.convert('1')
    image_binary_list= list(image_binary.getdata())
    image_binary_matrix = (np.resize(image_binary_list, image_binary.size)!=255)*1 #thaks to mali
    
    return image_binary_matrix
    
#image = image_converter ('Test_images/Sierpinski_gasket.gif')
image = image_converter ('Test_images/2010-05-01_ORNEK-77_013.jpg')
#image = np.ones((1500,1500))
slope =  fr.slope_finder(image)

print slope
    