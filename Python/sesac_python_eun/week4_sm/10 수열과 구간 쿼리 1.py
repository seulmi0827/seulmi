def solution(arr, queries):
    for s,e in queries:
        arr = arr[:s] + [i + 1 for i in arr[s:e+1]] + arr[e+1:]
    return arr
