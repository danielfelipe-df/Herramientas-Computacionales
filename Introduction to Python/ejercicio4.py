#!/usr/bin/python3
# -*- coding: utf8 -*-
a=[5,6,7,8,9,0,9,8,7,6,5]

def orden(a):
    n=0
    while(n<len(a)):
        m=n+1
        while(m<len(a)):
            if a[n]>a[m]:
                a[n],a[m] = a[m],a[n]
            m+=1
        n+=1
    return a
print orden(a)
