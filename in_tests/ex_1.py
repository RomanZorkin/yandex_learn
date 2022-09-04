import difflib as dif

#alice = input()
#zeliboba = input()
alice = 'ABCBCYA'
zeliboba = 'ZBBACAA'

name_len = len(alice)
tags = 'PSI'
result = str()
for al_num in range(name_len):
    if alice[al_num:al_num+1] == zeliboba[al_num:al_num+1]:
        result += 'P'
    else:
        result_2 = str()
        for zel_num in range(al_num, name_len):
            if zeliboba[al_num:al_num+1] not in zeliboba[al_num-1::-1]:
                if zeliboba[al_num:al_num+1] in alice[al_num::-1]:
                    result_2 = 'S'
                    break
            print(alice[zel_num:zel_num+1], zeliboba[al_num:al_num+1])
            if alice[zel_num:zel_num+1] == zeliboba[al_num:al_num+1]:
                if not alice[zel_num:zel_num+1] == zeliboba[zel_num:zel_num+1]:
                    result_2 = 'S'
                    break
            result_2 = 'I'
        result += result_2 
print(result)

good = 'IPSSPIP'