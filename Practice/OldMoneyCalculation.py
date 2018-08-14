import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def toDec(m):
    decCons = [10000,100,1]
    dec=0
    for z in range(len(m)):
        cur = m[z]
        dec += int(cur[0:len(cur)-1]) * decCons[z]
    return dec

def toFormat(m):
    decCons = [10000,100,1]
    g = str(m//decCons[0])+"G "
    s = str((m%decCons[0])//decCons[1])+"S "
    b = str((m%decCons[0])%decCons[1])+"B "
    return g+s+b

money = input()
price = input()
m = toDec(money.split(' '))
p = toDec(price.split(' '))
res = m-p
print(toFormat(res).strip())