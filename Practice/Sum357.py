import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
s=0
for i in range(3,n) :
    if (i%3==0) or i%5==0 or i%7==0 : 
        s+=i
print (s)