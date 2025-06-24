def solution(a, b, c, d):
    key = [1, 2, 3, 4, 5, 6]
    result = dict(zip(key, [0] * 6))
    result[a] += 1
    result[b] += 1
    result[c] += 1
    result[d] += 1
    for p in key:
        if result[p] == 4:
            return 1111 * p
        
        elif result[p] == 3:
            for q in key:  
                if q != p and result[q] == 1:  
                    return (10 * p + q) ** 2
        elif result[p] == 2:
            for q in key:
                if q !=p and result[q] == 2:
                    return (p+q) * abs(p-q)
                elif q !=p and result[q] == 1:
                    for r in key:
                        if r != p and r!=q and result[r] ==1:
                            return q * r
        else:
            if len([p for p in key if result[p] != 0]) == 4:
                return min([p for p in key if result[p] != 0])
