def solution(s):
    result = 0
    for i in s:
        if i == '(':
            result +=1
        else:
            result -=1
            if result < 0 :
                return False
    return result ==0
