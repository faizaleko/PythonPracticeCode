# INPUT : Second (n)
# OUTPUT : Readable time format {day}d {hour}h {minute}m {second}s

n = int(input())
d = n//86400
h = (n%86400)//3600
m = ((n%86400)%3600)//60
s = ((n%86400)%3600)%60
tm = ""
if d != 0:
    tm+=str(d)+"d "
if h != 0:
    tm+=str(h)+"h "
if m != 0:
    tm+=str(m)+"m "
if s != 0:
    tm+=str(s)+"s "
print(tm.strip())