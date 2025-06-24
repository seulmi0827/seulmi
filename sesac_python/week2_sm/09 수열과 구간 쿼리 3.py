def solution(arr, queries):
    for idx in range(len(queries)):
        i, j = queries[idx]
        arr[i],arr[j] = arr[j],arr[i]
    return arr
