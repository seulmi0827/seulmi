def solution(arr):
    a = [2**i for i in range(0,11)]
    if len(arr) in a:
        return arr
    else:
        a.append(len(arr))
        for idx,value in enumerate(sorted(a)):
            if value == len(arr):
                target = idx + 1
        while len(arr) < sorted(a)[target]:
            arr.append(0)
        return arr
