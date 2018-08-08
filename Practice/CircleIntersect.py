import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]
n = int(input())
k=0
for i in range(n):
    x, y, r = [int(j) for j in input().split()]
    if (a-x)**2 + (b-y)**2 <= r**2: k+=1 #Point to Point formula

print(k)