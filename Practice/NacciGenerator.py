#Currently use tetra
n=[0,0,0,1] #modify this one to fibo or any nacci
for i in range(int(input())-4):
    n+=[sum(n[-4:])]
print(sum(n))