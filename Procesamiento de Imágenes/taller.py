from scipy.misc import imread
import numpy as np
import pylab as pyl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage as nd

image = imread("Bolas1.tif", mode='L')
print(type(image))
print(image)
plt.imshow(image, cmap='gray')
plt.show()

im_filtrada = nd.median_filter(image,(3,3))
print(type(im_filtrada))
print(im_filtrada)
plt.imshow(im_filtrada, cmap='gray')
#plt.show()

imbin = pyl.where(image<50,0,255)
print(type(imbin))
print(imbin)
plt.imshow(imbin, cmap='gray')
plt.show()

def borders(jpg):
    kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    vertical = nd.convolve(jpg, kernel)
    print(type(vertical))
    print(vertical)
    plt.imshow(vertical, cmap='gray')
    plt.show()
    
    kernel = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    horizontal = nd.convolve(jpg, kernel)
    print(type(horizontal))
    print(horizontal)
    plt.imshow(horizontal, cmap='gray')
    plt.show()

    return vertical, horizontal

vertical, horizontal = borders(imbin)
labels1 , number_labels1 = nd.label(imbin)
plt.imshow(labels1)
plt.colorbar()
plt.show()
print(number_labels1)
#print(labels1)
for i in range(number_labels1):
    centers = nd.center_of_mass(imbin, labels1, i+1)
    print(centers)
labels2 , number_labels2 = nd.label(vertical)
#print(number_labels2)
#print(labels2)
labels3 , number_labels3 = nd.label(horizontal)
#print(number_labels3)
#print(labels3)
#borders(image)
#borders(im_filtrada)
