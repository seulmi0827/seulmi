def solution(arr):
    n = len(arr)
    result = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                result = 0
    return result
