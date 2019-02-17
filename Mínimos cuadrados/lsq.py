import numpy as np
from numpy.linalg import inv,lstsq
from pylab import *
#
x=np.linspace(0,15,100)
y=10+4.566*x+0*x**2+10*np.random.random(x.shape)


f=[]
f.append(lambda x:np.ones_like(x))
f.append(lambda x:x)
f.append(lambda x:x**2)

Xt=[]

for fu in f:
    Xt.append(fu(x))
    
Xt= np.array(Xt)
X=Xt.transpose()



a = np.dot(np.dot(inv(np.dot(Xt,X)),Xt),y)
print(a)

#print(lstsq(X,y)[0])
#print(X)

plot(x,y)

y1=0
for n,ac in enumerate(a):
	y1=y1+ac*x**n
plot(x,y1)
show()
