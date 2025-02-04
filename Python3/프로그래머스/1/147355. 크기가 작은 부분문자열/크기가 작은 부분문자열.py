def solution(t, p):
    i_result = []
    for i in range(len(t)-len(p)+1):
        i_result.append(int(t[i:i+len(p)]))
    j_result = []
    for j in i_result:
        if j <= int(p):
            j_result.append(j)
    return len(j_result)