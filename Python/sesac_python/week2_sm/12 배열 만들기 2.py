def solution(l, r):
    result = []
    for i in range(l,r+1):
        if i % 5 == 0:
            TF =1
            for j in str(i):
                TF*=(j in ('0','5'))
            if TF==1:
                result.append(i) 
    return result if len(result)!=0 else [-1]
