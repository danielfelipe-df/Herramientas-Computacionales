#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print ('Primer punto')
from math import cos
from math import sin
a=input("Escribe un número: ")
print 'Cos({}) ={:6.3f}'.format(a,cos(a))
print 'Sin({}) ="{:6.3f}"'.format(a,sin(a)),'\n'

print ('Segundo punto')
a,b=input("Escribe la parte real e imaginaria de un número complejo: ")
z=complex(a,b)
print 'El cuadrado del módulo del número complejo es:',abs(z)*abs(z),'\n'

print ('Tercer punto')
a,b,c,d,e=input("Escribe 5 números: ")
print 'El cuadrado de{}es'.format(a,a*a)
print 'El cuadrado de{}es'.format(b,b*b)
print 'El cuadrado de{}es'.format(c,c*c)
print 'El cuadrado de{}es'.format(d,d*d)
print 'El cuadrado de{}es'.format(e,e*e),'\n'

print ('Cuarto punto')
a=raw_input("Escribe un número: ")
print 'El cuadrado de',a,'es',float(a)*float(a),'\n'

print ('Quinto punto')
b=raw_input("Escribe una palabra: ")
print b[::-1]



print ('Séptimo punto')
a=raw_input("Escribe una palabra: ")
print a.upper()
