from pylab import *

k = .0
m = 1
dt = 0.1

def dvdt(x):
	return -k*x/m
	
def dxdt(v):
	return v

x = .0
v = 0.
t = 0.

xl=[]
vl=[]
tl=[]

for i in range(1000):
	xl.append(x)
	vl.append(x)
	tl.append(x)
	vo=v
	xo=x
	x=x+dt*dxdt(vo)
	v=v+dt*dvdt(xo)
	t=t+dt
	
plot(tl,xl,label="pos")
plot(tl,vl,label="vel")
legend()
show()
