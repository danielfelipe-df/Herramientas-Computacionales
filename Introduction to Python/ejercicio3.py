#!/usr/bin/python3
# -*- coding: utf8 -*-

print('Primer punto')
a=input("Escribe un número: ")

def sumatoria(a):
    if a==1:
        return 1
    else:
        return a+sumatoria(a-1)
print sumatoria(a),'\n'

print ('Segundo punto')
a,b=input('Escribe un número y su potencia: ')

def potencia(a,b):
    if b==0:
        return 1
    else:
        return a*potencia(a,b-1)
print potencia(a,b)
    
