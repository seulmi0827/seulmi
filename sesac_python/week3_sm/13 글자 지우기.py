def solution(my_string, indices):
    result = "".join([j[1] for j in list(enumerate(my_string)) if j[0] not in indices])
    return result
