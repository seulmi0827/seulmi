def solution(arr, flag):
    x = []
    for idx ,booleans in enumerate(flag):
        if booleans: x.extend([arr[idx]]*arr[idx]*2)
        else : x = x[:len(x)-arr[idx]]  
    return x
