def solution(order):
    return sum([5000 if 'cafelatte' in i else 4500 for i in order])
