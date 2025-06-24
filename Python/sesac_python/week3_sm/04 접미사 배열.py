def solution(my_string):
    result = []
    for idx in range(len(my_string)):
        result.append(my_string[idx:])
    return sorted(result)
