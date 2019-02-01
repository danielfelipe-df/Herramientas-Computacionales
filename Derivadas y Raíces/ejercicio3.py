import pylab as pyl
from math import *

def bisectriz(a,b,f,eps):
    contador = 0
    c = (a+b)/2
    x = [contador]
    y = [abs(f(c))]
    while(abs(f(c)) > eps):
        if (f(c)>0):
            a=c
        else:
            b=c
        c = (a+b)/2
        contador = contador + 1
        x.append(contador)
        y.append(abs(f(c)))
    print(contador)
    return (f(c),x,y) 

a = 3
b = 3.3
f = sin
eps = 1e-10

(value,x,y)=bisectriz(a,b,f,eps)
print(value)
pyl.plot(x,y)
pyl.show()











