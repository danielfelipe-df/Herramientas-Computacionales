from scipy.misc import imread
import numpy as np
#from pylab import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = imread("Bolas1.tif", mode='L')
print(type(image))
print(image)
plt.imshow(image, cmap='gray')
plt.show()
