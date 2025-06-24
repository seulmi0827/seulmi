def solution(n):
    result = [n]
    while True:
        if result[-1] % 2 ==0:
            last = result[-1]/2
            if last !=1:
                result.append(int(last))  
            elif last ==1:
                result.append(int(last)) 
                break
        else:
            last = 3*result[-1]+1
            result.append(int(last))
    return result
