def solution(s):
    result = True
    if len(s) not in (4,6):
        result = False
    for i in s:
        if i not in "1234567890":
            result = False
    return result