def solution(arr,queries):
    result2 = []
    for sek in queries:
        s,e,k = sek
        result = []
        result.extend([j for j in arr[s:e+1] if j > k])
        if len(result) == 0:
            result2.append(-1)
        else:
            result2.append(min(result))
    return result2
