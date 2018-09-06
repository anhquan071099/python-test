import sys
import os
import random
import math

def PTB2(a,b,c):
    delta = float(b*b-4*a*c)
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    return x1,x2,delta

print("input a: ")
x = int(input())
print("intput b: ")
y = int(input())
print("input c: ")
z = int(input())



# PTB2(x,y,z)
# print(x1,x2,delta)                          
                    

