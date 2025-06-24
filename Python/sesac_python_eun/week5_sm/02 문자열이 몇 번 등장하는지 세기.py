def solution(myString, pat):
    result = 0
    for idx, mystr in enumerate(myString):
        if myString[idx:idx+len(pat)] == pat:
            result +=1
    return result
