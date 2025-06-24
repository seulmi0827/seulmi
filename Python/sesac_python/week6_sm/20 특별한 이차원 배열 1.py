def solution(n):
    total = []
    for i in range(n):
        result = [0]*n
        result[i] = 1
        total.append(result)
    return total
