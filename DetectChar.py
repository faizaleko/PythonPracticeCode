k=input()
a=''
if k.isupper():
    for i in range(ord('A'),ord(k)+1):a+=chr(i)
elif k.islower():
    for i in range(ord('a'),ord(k)+1):a+=chr(i)
else:
    for i in range(ord('0'),ord(k)+1):a+=chr(i)
print(a)