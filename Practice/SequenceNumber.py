import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input()) # START Number
b = int(input()) # Multiple diff
c = int(input()) # Column
d = int(input()) # Row
rs = list(range(a,a+(b*c*d),b))
for z in range(0,len(rs),c):
    print(*rs[z:z+c],sep=" ")
        