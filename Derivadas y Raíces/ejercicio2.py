import pylab as pyl
from math import * 

def segunda_deriv(f,a,h=1e-5):
    return (f(a+h)+f(a-h)-(2*f(a)))/(h*h)

def grafica(f,ddf,a,h0,hmax,deltah):
    h=[]
    dxl=[]
    while (h0 > hmax):
        h.append(h0)
        dxl.append(abs((ddf(a)-segunda_deriv(f,a,h0))/ddf(a)))
        h0=h0*deltah
    pyl.plot(h,dxl)
    pyl.show()

f = exp
#La siguiente función g se define para poderle poner el negativo al seno, pues no se puede usar -sin
#g= lambda x: -sin(x)
ddf = exp
a = pi/2
h0 = 1e-1
hmax = 1e-6
deltah = 0.5

print (segunda_deriv(f,a,h0))
grafica(f,ddf,a,h0,hmax,deltah)
