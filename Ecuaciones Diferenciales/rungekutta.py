from pylab import *
import math
l = 5
g = 9.8
dt = 0.01

def dwdt(x):
	return -g*math.sin(x)/l
	
def dxdt(w):
	return w

x = math.pi/4
w = 0
t = 0

xl=[]
wl=[]
tl=[]

for i in range(10000):
	xl.append(x)
	wl.append(w)
	tl.append(t)
	wo=w
	xo=x
	
	k1 = dt*dxdt(wo)
	j1 = dt*dwdt(xo)
	
	k2 = dt*dxdt(wo + j1/2)
	j2 = dt*dwdt(xo + k1/2)
	
	k3 = dt*dxdt(wo + j2/2)
	j3 = dt*dwdt(xo + k2/2)
	
	k4 = dt*dxdt(wo + j3)
	j4 = dt*dwdt(xo + k3)
	
	x=x + k1/6 + k2/3 + k3/3 + k4/6
	w=w + j1/6 + j2/3 + j3/3 + j4/6
	t=t+dt
	
plot(tl,xl,label="theta")
plot(tl,wl,label="omega")
legend()
show()
