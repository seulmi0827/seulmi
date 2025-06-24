def solution(number):
    answer = sum([int(i) for i in number]) % 9 
    return answer
