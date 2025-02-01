def solution(arr):
    min_arr = min(arr)
    return [i for i in arr if i != min_arr] if len(arr) != 1 else [-1] 