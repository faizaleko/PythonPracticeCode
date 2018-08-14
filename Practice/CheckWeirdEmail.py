import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
em=[]
em.append("<steve@example.com>")
em.append("<john.doe@codingame.com>")
em.append("<un{ba[lan)cea'ble@xxx.>")
em.append("[(balanced)@example.com]")
em.append("<inigo montoya@buttercup.net>")
em.append("<bill@example>")
em.append("<timey!uucp!gw!ucb>")

valist = []
for i in em:
    line = i
    # print(line[0]+line[len(line)-1])
    if line[0] == '<' and line[len(line)-1] == '>':
        se = line.split('@')
        m = len(se)
        if m == 2:
            if ' ' not in se[0] and '.' in se[1]:
                valist.append(line)

print(*valist,sep='\n')
print(len(valist))