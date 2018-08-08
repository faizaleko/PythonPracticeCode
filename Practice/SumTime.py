import sys
import math

# INPUT 
# Time Limit (L) ex: 00:00:25
# N = N time ex: 2
# S Time 1 (S1) ex: 00:00:15
# S Time 2 (S2) ex: 00:00:05
# OUTPUT
# TRUE if L <= S1+S2
# FALSE if L > S1+S2

def f(time):
    h,m,s = map(int, time.split(':'))
    return h*3600 + m*60 + s

l = f(input())
n = int(input())
s = 0
for i in range(n):
    s += f(input())
print('true' if s <= l else 'false')