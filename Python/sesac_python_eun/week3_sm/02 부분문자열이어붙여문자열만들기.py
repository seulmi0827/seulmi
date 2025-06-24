def solution(my_strings, parts):
    result = ''
    for idx in range(len(my_strings)):
        result += my_strings[idx][parts[idx][0]:parts[idx][1]+1]
    return result
