import os
import sys
import math
import random


def QUADRATIC_EQUATION_2(a, b, c):
    delta = float(b*b-4*a*c)
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    return  print("x1 = {}, x2={}".format(x1,x2))


print("input a: ")
x = int(input())
print("intput b: ")
y = int(input())
print("input c: ")
z = int(input())

if x == 0:
    print("quaratic have 1 no is: ",float(-z/y) )
elif x != 0:
    QUADRATIC_EQUATION_2(x, y, z)
    
