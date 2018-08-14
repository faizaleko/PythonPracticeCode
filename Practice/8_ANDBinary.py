# INPUT : Binary n_1, n_2
# OUTPUT : n_1 AND n_2

n_1 = input()
n_2 = input()
print(str(format(int(n_1, 2) & int(n_2, 2), "b")).zfill(len(n_1)))

# Another solution
# res = ""
# for z in range(len(n_1)):
#     if (int(n_1[z])+int(n_2[z])) == 2:
#         res+="1"
#     elif (int(n_1[z])+int(n_2[z])) == 1:
#         res+="0"
#     else:
#         res+="0"
# print(res)