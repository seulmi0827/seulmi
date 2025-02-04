def solution(arr):
    last_i = -1
    result = []
    for i in arr:
        if i != last_i:
            result.append(i)
        last_i = i    
    return result