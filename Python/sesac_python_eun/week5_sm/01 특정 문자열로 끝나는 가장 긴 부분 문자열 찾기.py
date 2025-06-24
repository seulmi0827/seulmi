def solution(myString, pat):
    for idx , mystr in enumerate(myString):
        if mystr == pat[-1]:
            end = idx+1
    return myString[:end]
