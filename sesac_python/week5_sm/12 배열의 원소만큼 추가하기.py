def solution(arr):
    result = []
    for i in [[i]*i for i in arr]:
        result.extend(i) 
    return result
