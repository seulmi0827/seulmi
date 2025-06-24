def solution(n, control):
    num = n
    for i in control:
        if i == "w":
            num +=1
        elif i == "s":
            num -=1
        elif i == "d":
            num +=10
        elif i =="a":
            num -= 10
    return num
