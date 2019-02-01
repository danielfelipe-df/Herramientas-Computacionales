import numpy as np
import pylab as pyl

def simpson(f,x0,x1,n):
    x = np.linspace(x0,x1,n)
    fx = f(x)
    x_par = np.linspace(x0,x1,n/2)
    fx_par = f(x_par)
    sumatorias = 4*np.sum(fx) - 2*np.sum(fx_par) - 2*(f(x0)+f(x1))
    integral = (x1-x0)*sumatorias/(3*n)
    return integral

f= np.sin
x0 = 0
x1 = 3.14159
n = 10000
print(simpson(f,x0,x1,n))

i=1
y=[]
x=[]
n1= int(n/10)
while(i<=n):
    y.append(abs(2-simpson(f,x0,x1,i)))
    x.append(i)
    i += 1
pyl.plot(x[n1:n],y[n1:n])
pyl.show()
