import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
print('#'*n)
for z in range(1,n*2,2):
    print(('#'*z).center(n*2,' '))

for z in range((n*2)-1,0,-2):
    print(('#'*z).center(n*2,' '))