liz=[]
n = int(input())
for z in range(n):
    z = int(input())
    liz.append(z)

rs=[]
for c in liz:
    if (c%2 == 0):
        rs.append("even")
    else:
        rs.append("odd") 

if rs.count("even") > rs.count("odd"):
    print(liz[rs.index("odd")])
else:
    print(liz[rs.index("even")])