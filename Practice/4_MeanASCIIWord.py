import sys
import math

# INPUT : Char/String ex: abc
# OUTPUT : The Mean of ASCII a(97) + b(98) + c(99) = 294/3 = 98

s = input()
print(sum(map(lambda x : ord(x),s))/len(s))