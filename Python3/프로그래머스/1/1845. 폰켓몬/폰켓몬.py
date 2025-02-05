def solution(nums):
    result = dict()
    for i in set(nums):
        result[i] = 0
    for j in nums:
        result[j] += 1
    if len(nums)/2 > len(result):
        return len(result)
    else:
        return len(nums)/2
        