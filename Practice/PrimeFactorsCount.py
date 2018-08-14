import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def isPrime(n):
    isPrime = True
    for num in range(2, n):
        if n % num == 0:
            isPrime = False
    return(isPrime)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(factors)
    
rs=[]
a, b, n = [int(i) for i in input().split()]
for z in range(a,b+1):
    if prime_factors(z) == n:
        rs.append(z)

if len(rs) == 0:
    print("NONE")
else:
    print(*rs,sep=' ')