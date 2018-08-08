import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
sums = 0
for z in range(len(str(x))):
    sums += int(str(x)[z])

isValid = True
for y in range(len(str(x))):
    currInt = int(str(x)[y])
    if currInt <= (sums-currInt):
        isValid = False
        break
    sums-=currInt

if isValid:
    print("Magic Number : "+str(x))
else:
    print("Not Magic Number")       