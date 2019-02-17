#!/usr/bin/python3
# -*- coding: utf8 -*-

a=input("Inserte un número mayor a 0: ")

def f1(a):
    factorial=1
    n=1
    while (n<=a):
        factorial*=n
        n+=1
    return factorial
print f1(a)


def f2(a):
    if a==1:
        return 1
    else:
        return a*f2(a-1)
print f2(a)

