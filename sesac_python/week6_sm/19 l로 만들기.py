def solution(myString):
    result = ''
    for i in myString:
        if i in ('a','b','c','d','e','f','g','h','i','j','k'):
            i = 'l'
        result += i
    return result

##다른사람풀이
def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)
