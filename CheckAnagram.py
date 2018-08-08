import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s1, s2 = input().split()
print(1 if sorted(s1) == sorted(s2) else 0)

# Other solution
# if s1[::-1] == s2:
#     print("Anagram")
# else:
#     print("Not Anagram")
