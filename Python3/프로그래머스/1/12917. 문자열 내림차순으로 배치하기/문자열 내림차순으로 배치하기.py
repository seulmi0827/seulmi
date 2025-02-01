def solution(s):
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = small.upper()
    alps = big + small
    num2alp = dict()
    alp2num = dict()
    for num, alp in enumerate(alps):
        num2alp[num] = alp
        alp2num[alp] = num

    result = []
    for num in sorted([alp2num[i] for i in s],reverse=True):
        result.append(num2alp[num])

    return ''.join(result)