# Runner for fracdim module
__author__ = "Kivanc Esat"
__copyright__ = ""
__credits__ = ["Kivanc Esat, Mehmet Ali Anil"]
__license__ = ""
__version__ = "0.0.2"
__maintainer__ = "Kivanc Esat"
__email__ = "esat [at] itu.edu.tr"
__status__ = "Production"

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
    