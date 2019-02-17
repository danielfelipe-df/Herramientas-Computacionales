import numpy as np
import pylab as pyl
def integral(f,x0,x1,n=100):
    x = np.linspace(x0,x1,n)
    fx = f(x)
    integral = (x1-x0)*(np.sum(fx)-((fx[0]+fx[n-1])/2))/n
    return integral

f = np.sin
i=1
n=100
y = []
x = []
while(i<=n):
    y.append(abs(2-integral(f,0,3.14159,i)))
    x.append(i)
    i += 1
#yl.plot(x,y)
#yl.show()
y1 = abs(2-integral(f,0,3.14159,np.linspace(1,n,n)))
print(y1)

