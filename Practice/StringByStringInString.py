import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
z=""
c = "065066067"
while len(c) != 0:
    z+=chr(int(c[:3]))
    c=c[3:]
print(z)