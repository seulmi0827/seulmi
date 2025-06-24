def solution(my_string):
    upper = [i for i in 'abcdefghijklmnopqrstuvwxyz'.upper()]
    lower = [j for j in 'abcdefghijklmnopqrstuvwxyz']
    atoz = list(enumerate(upper+lower))
    result = [0]*52
    for i in my_string:
        for j in atoz:
            if i == j[1]:
                result[j[0]] += 1
    return result
