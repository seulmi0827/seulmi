def solution(x, n):
    if x ==0:
        return [0]*n
    elif x > 0:
        return [i for i in range(x,x*n+1,x)]
    else:
        return [i for i in range(x,x*n-1,x)]
