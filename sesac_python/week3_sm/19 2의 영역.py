def solution(arr):
    idx = [i for i in range(len(arr)) if arr[i]==2]
    if len(idx)==0 :
        return [-1] 
    return arr[idx[0]:idx[-1]+1]
