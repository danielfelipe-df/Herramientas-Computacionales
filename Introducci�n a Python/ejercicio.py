#!/usr/bin/python
# -*- coding: utf8 -*-
a=input("Escriba un numero: ")

print "Primer punto"
b=0
while b<a:
	print b,"-",
	b+=2
print "\n"

print "Segundo punto"
suma=0
i=1
while i<=a:
	suma+=i
	i+=1
print "La suma es: ", suma, "\n"

print "Tercer punto"
factorial=1
i=1
while i<=a:
	factorial*=i
	i+=1
print "Su factorial es: ", factorial, "\n"

print "Cuarto punto"
contador=2
j=1
i=1
print j, i,
while contador<a:
	fibonacci= i+j
	print fibonacci,
	j=i
	i=fibonacci
	contador+=1
print "\n"			

print "Quinto punto"
i=2
contador=0
c=a/2
while i<=c:
	if(i%a==0):
		contador+=1
	i+=1
if contador==0:
	print a, " es primo."
else:
	print a, " no es primo"
print "\n"
