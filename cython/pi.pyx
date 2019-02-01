import math

def pi_viete(n):
	a = math.sqrt(2) 
	producto = a / 2
	for i in range(n):
		a = math.sqrt(2 + a) 
		producto = producto * a / 2
	return 2/producto
	
	
def pi_leibniz(n):
	suma = 0
	for i in range(1,n+1):
		if(i%2 == 0):
			suma = suma - (1/i)
		else:
			suma = suma + (1/i)
	return 4.0*suma
	

pi_def1 = pi_viete(50000)
pi_def2 = pi_leibniz(500000)

print(pi_def2)
print(pi_def1)
