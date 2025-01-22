def solution(quiz):
    result = []
    for i in quiz:
        if '-' in i.split():
            if int(i.split()[0]) - int(i.split()[2]) == int(i.split()[4]):
                result.append("O")
            else:
                result.append("X")
        else:
            if int(i.split()[0]) + int(i.split()[2]) == int(i.split()[4]):
                result.append("O")
            else:
                result.append("X")
    return result
            