import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Sum the Even Number
# Ex: N=4, then SUM 2,4,6,8 ==> 20
n = int(input())
oriNum = n
sumNum = 0
isZero = False
if (n != 0):
    sumNum += n
    if (n%2 == 0):
        for z in range(3):
            if (n-2) == 0:
                isZero = True

            if ((n-2) != 0) and not isZero:
                sumNum += (n-2)
                n -= 2
            else:
                sumNum += (oriNum+2)
                oriNum += 2
        print(sumNum)
    else:
        print("Not Even Number")
else:
    print("Zero Number")



