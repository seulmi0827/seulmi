def solution(ineq, eq, n, m):
    if ineq == '<':
        if eq =='=':
            return int((n<=m)is True)
        else:
            return int((n<m)is True)
    else:
        if eq =='=':
            return int((n>=m)is True)
        else:
            return int((n>m)is True)
