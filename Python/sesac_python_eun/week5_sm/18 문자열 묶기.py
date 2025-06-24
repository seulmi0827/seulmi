def solution(strArr):
    result = [0]*31
    for i in [len(i) for i in strArr]:
        result[i] += 1
    return sorted(result)[-1]
