
def solution(arr):
    i = 0
    while True : 
        result = []
        for j in arr :
            if j>=50 and j%2==0:
                result.append(int(j/2))
            elif j<50 and j%2==1:
                result.append(int(j*2)+1)
            else:
                result.append(j)
        if arr == result:
            return i
            break
        else: 
            arr = result
            i += 1
