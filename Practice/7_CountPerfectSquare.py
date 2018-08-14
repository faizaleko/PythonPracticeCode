import sys
import math

# INPUT : range A - B ex:1-9
# OUTPUT : there is 3 perfect square (1,4,9) from 1-9

def perfect_square(x):
    y = x**(1/2)
    if y%1 == 0:
        return True
    else:
        return False

co=0
a = int(input())
b = int(input())
for z in range(a,b+1):
    print(z)
    if perfect_square(z):
        co+=1
print(co)