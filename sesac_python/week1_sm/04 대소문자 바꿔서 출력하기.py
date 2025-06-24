str = input()
for i in range(0,len(str)):
    if 1 <= len(str) <=20:
        if str[i].upper() == str[i]:
            print (str[i].lower(),end='')
        else:
            print (str[i].upper(),end='')
    else:
        pass
