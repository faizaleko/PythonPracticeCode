# INPUT : Codingame
# OUTPUT : 
# Codingame
# eCodingam
# meCodinga
# ameCoding
# gameCodin
# ngameCodi
# ingameCod
# dingameCo
# odingameC
# Codingame

s = input()
for z in range(1,len(s)+1):
    print(s[len(s)-z::]+s[0:len(s)-z:])