from scipy.misc import imread
from pylab import *

imc = imread("lena_std.tif")
#En el caso de que en python3 no corra, desativar el siguiente comado
imc.setflags(write=1)
imb = imread("lena_bw.tif")
imr = imread("lena_bw_noise_bin.tif")

print(imc.shape, imb.shape)
imc[:,:,0] = 0
imc[:,:,2] = 0
imc[200:300,200:300] = 255
imbin = where(imb<200,0,255)
figure()
imshow(imbin, cmap = "gray")
show()
#imn = 255*ones(imc.shape, dtype="uint8")-imc
#imshow(imn)
#imsave("negativo.png", imn)
#show()
#imshow(imr)

#figure()
#imshow(imb, cmap="gray")
#colorbar()
#show()
