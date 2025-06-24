def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) == sum(arr2):
            return 0
        return 1 -2*(sum(arr1) < sum(arr2))
    return 1 -2*(len(arr1) < len(arr2))
