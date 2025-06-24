def solution(n):
    i = 0
    result = ''
    while i != n:
        if i % 2 == 0:
            result += '수'
            i += 1
        else:
            result += '박'
            i += 1
    return result