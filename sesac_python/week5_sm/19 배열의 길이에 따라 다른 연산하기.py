def solution(arr, n):
    if len(arr) % 2 ==1:
        return [i+n if idx%2==0 else i for idx,i in enumerate(arr)]
    return [i+n if idx%2==1 else i for idx,i in enumerate(arr)]
