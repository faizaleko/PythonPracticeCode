import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# val = 0
# for z in range(len(s)):
#     val+=ord(s[z])
# print(math.floor(val/len(s)))

print(sum(map(lambda x : ord(x),s))/len(s))