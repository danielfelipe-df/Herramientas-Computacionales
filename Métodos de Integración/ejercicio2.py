import numpy as np
import pylab as pyl

def punto_medio(f,x0,x1,n=100):
    x = np.linspace(x0,x1,n) + ((x1-x0)/n)
    fx = f(x)
    integral = ((x1-x0)/n)*(np.sum(fx))
    return integral

f = np.sin
x0 = 0
x1 = 3.14159
n = 100000
print(punto_medio(f,x0,x1,n))
i = 1
y = []
x = []
while(i<=n):
    y.append(abs(2-punto_medio(f,x0,x1,i)))
    x.append(i)
    i = i+1

pyl.plot(x[10000:100000],y[10000:100000])
pyl.show()
