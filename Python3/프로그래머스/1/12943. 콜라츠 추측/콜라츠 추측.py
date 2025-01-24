def solution(num):
    i = 0
    while True:
        if num ==1:
            i = 0
            break
        elif num % 2 == 0:
            num = num / 2
            i +=1
            if num ==1:
                break
        else:
            num = num * 3 +1
            i +=1
            if num ==1:
                break
        if i == 500:
            i = -1
            break
    return i