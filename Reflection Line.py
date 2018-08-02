import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# a = axis (x or y)
# b = reflection point
# n = n coordinat inputed
a = input()
b = int(input())
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if (a == 'x'):
        y = b-abs(b-y) if (y>b) else b+abs(b-y)
    else:
        x = b-abs(b-x) if (x>b) else b+abs(b-x)
    print(x,y,end=' ')
    print()