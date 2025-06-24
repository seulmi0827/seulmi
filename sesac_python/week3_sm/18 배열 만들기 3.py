def solution(arr, intervals):
    i = []
    for a,b in intervals: i.extend(arr[a:b+1])
    return i
