import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# INPUT = Hello World
# OUTPUT = olleH dlroW

s = input()
# newStr = ""
# list1 = list(s.split())
# for z in list1:
#     newStr += z[::-1] + " "
# print(newStr.strip())

# Smart
li = list(s.split())
print(" ".join(map(lambda x : x[::-1], li)))