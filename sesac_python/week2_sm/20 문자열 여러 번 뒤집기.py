#슬라이싱 이용x
def solution(my_string, queries):
    for i in queries:
        start ,end = i
        result1 = ''
        result2 = ''
        result3 = ''
        for k in range(len(my_string)):
            if k < start:
                result1 += my_string[k]
            elif start <= k <=end:
                result2 += my_string[k]
            elif end < k :
                result3 += my_string[k]
        my_string = result1 + result2[::-1] + result3

    return my_string
#슬라이싱 이용
def solution(my_string, queries):
    for i in queries:
        start ,end = i
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    return my_string
