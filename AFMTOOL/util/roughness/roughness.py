""" 
Function to calculate roughness(Ra) of a square region
Inputs- (x,y) coordinate the center of square and L, side length of square, in micrometer. 

Machine-learning algorithm in util/shape_recogniser will give the function the center of the Cu connections for input. 
Side length of square will be set by user

From https://www.olympus-ims.com/en/metrology/surface-roughness-measurement-portal/parameters/#!cms[focus]=007, 
Roughness Average (Ra) is given by average of absolute values of deviation from the mean of a given sample. 
In Numpy's terminology it's Mean Absolute Deviation from mean (https://www.geeksforgeeks.org/absolute-deviation-and-absolute-mean-deviation-using-numpy-python/)
"""

import pySPM
#print(pySPM.__version__)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from IPython import display

from numpy import mean, absolute

def find_ra(array, x,y, is_copper=True):
    """ 
    Returns average roughness of region of copper contact centered at (x,y), 
    with default side length of region = 13 pixels = 1.016 micrometer for copper,
    and 25 pixels for polymer, 
    so that the region extends 6 pixels/12 pixels in each direction from the center piece. 
    
    Coordinates in numpy array generated by pySPM matches orientation of image generated
    """
    
    range =6 if is_copper else 12
    
    #Define sample area to calculate roughness 
    #used min, max in case selected center is too close to the borders
    sample = array[min(x-range,0):max(x+range+1, 256), min(x-range,0):max(x+range+1, 256)] 

    
    return mean(absolute(sample - mean(sample)))


def excel_input_ra():
    return 0
    

