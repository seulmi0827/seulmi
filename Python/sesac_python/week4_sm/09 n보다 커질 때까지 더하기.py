def solution(numbers, n):
    start = 0
    for i in numbers: 
        start += i
        if start > n: 
            return start
