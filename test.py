import math
import sys
import random
import os


def plush(a, b, c):
    d = float((a+b+c)/3)
    return d


print ("input a: ")
a=int( input())
print("intput b: ")
b = int(input())
print("input c: ")
c = int(input())
print("d: ", plush(a,b,c))    
