def solution(str1,str2):
    str3 = str1 + str2
    a=[]
    total=''
    for i in range(len(str1)):
        a.extend([str3[i] , str3[i+len(str1)]])
    for i in a:
        total += i
    return total
