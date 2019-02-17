from pylab import *

TA=15E-6
FM=140E6
DF=40E6
VA=650
LBD=405E-9

MR= []

FF = linspace(1000,33000,300)

for FDS in FF:
	TScan = 1./FDS
	
	TBP = TA*DF
	
	Nspots=TBP*(1-TA/(TScan-TA))
	
	THB = LBD*FM/(2*VA)
	
	SCAN=LBD*DF/VA
	
	MR.append(Nspots*FDS)
	
plot(FF,MR)
show()
