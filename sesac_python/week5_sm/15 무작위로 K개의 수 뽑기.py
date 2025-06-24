def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    if len(result) >= k:
        return result[:k]
    else:
        return result + [-1]*(k-len(result))

            
