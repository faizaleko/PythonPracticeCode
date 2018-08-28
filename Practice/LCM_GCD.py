import sys
import math
from math import gcd

a=[]
n = int(input())
for i in input().split():
    m = int(i)
    a.append(m)

lcm = a[0]
for i in a[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print(lcm)