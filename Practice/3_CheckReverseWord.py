import sys
import math

# Check reverse word
# INPUT : 2 String ex: "world dlrow"
# OUTPUT : 1 if "world" is the reverse of "dlrow" 

s1, s2 = input().split()
print(1 if sorted(s1) == sorted(s2) else 0)

# Other Solution
# if s1[::-1] == s2:
#     print(1)
# else:
#     print(0)