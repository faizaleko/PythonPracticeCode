import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
p=""
a = input() # Encrypted String
b = input() # Decrypted String
c = ord(a[0])-ord(b[0])
for z in a:
    if ((ord(z)-c)-65) > 0:
        p+=chr(ord(z)-c)
    else:
        p+=chr(ord('Z')-abs(((ord(z)-c+1)-65)))

# Validation
print(p)
if p == b:
    print("true")
else:
    print("false") 