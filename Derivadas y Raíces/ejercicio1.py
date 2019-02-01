import pylab as pyl
from math import *

def deriv_ade(h,a,f):
    return (f(a+h)-f(a))/h

def deriv_cent(h,a,f):
    pass

def deriv_extra(h,a,f):
    pass

#Esta función guarda los datos y hace la gráfica
def grafica(h0,hmax,deltah,a,f,df):
    h=[]
    dxl=[]
    while(h0>hmax):
        h.append(h0)
        dxl.append(abs((df(a)-deriv_ade(h0,a,f))/df(a)))
        h0=h0*deltah
    pyl.plot(h,dxl)
    pyl.show()

h0=1e-1
hmax=1e-10
deltah=0.5
f1=exp
df1=exp
f2=cos
df2=sin
x=[0,1,10,100]

grafica(h0,hmax,deltah,x[0],f1,df1)
