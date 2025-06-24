def solution(s):
    result = []
    answer_len = len(s)
    i = 0
    while len(result) != answer_len:
        if s[i] ==' ':
            s = s[i+1:]
            i = 0
            result.append(' ')
        else:
            if i % 2 == 0:
                result.append(s[i].upper())
                i+=1
            else:
                result.append(s[i].lower())
                i+=1
    return ''.join(result)