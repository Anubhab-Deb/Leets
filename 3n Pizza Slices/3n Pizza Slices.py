# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:41:36 2026

@author: anubh
"""

n=int(input())
k=int(input())
m=n
size=list(map(int, input().split()))
size.sort()
size.reverse()
total=0
i=0
if len(size)!=3*n:
    print("error")
else:
    while m>0 and i<len(size):
        if m==n:
            total+=size[i]
            m-=1
            i+=1
        elif m<n and k>0:
            total+=size[i]
            m-=1
            k-=1
            i+=1
        elif m<n and k==0:
            i+=1
            if i>=len(size):
                break
            elif i<len(size):
                total+=size[i]
                m-=1
                i+=1

    print(total)