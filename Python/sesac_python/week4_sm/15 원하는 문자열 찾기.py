def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    for idx, mystr in enumerate(myString):
        if myString[idx:idx+len(pat)] == pat:
            return 1
    return 0 #idx가 필요할 때는 len쓰지말고 enumerate를 사용해보자
