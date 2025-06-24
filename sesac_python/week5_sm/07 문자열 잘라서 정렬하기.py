def solution(myString):
    result = myString.split('x')
    result2 = [i for i in result if i]
    result2.sort()
    return result2
