import sys
import math
from functools import reduce

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
student=[]
student.append("MadKnight 5.5 6.6 0.2")
student.append("dzik 9.9 8.8 7.7")
student.append("SamSi 6.0 6.0 9.9")
student.append("Lachrymosa 1.0 2.0 9.8")
student.append("BOSSY 6.0 6.1 6.2")
student.append("Crownie 6.6 5.5 7.7")
student.append("AlexeyRjeutski 5.5 6.6 7.7")
student.append("WickedMule 8.8 7.7 6.6")
student.append("EugenioToshiAmato 1.1 0.0 0.0")
student.append("RiccardoRossiMori 1.9 6.6 9.9")

di={}
for i in student:
    z = i.split()
    idz = z[0]
    del z[0]
    sumz = reduce(lambda x,y : float(x)+float(y), z)
    di[idz] = sumz

dsort = dict(sorted(di.items(), key=lambda x: x[1]))
# dsort = dict(sorted((value, key) for (key,value) in di.items()))
for z in dsort:
    print(dsort[z])