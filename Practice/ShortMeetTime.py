import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
list1 = []
for i in range(n):
    s, d = [int(j) for j in input().split()]
    list1.append(d/s)

print(min(list1)*60)