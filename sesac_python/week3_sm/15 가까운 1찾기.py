def solution(arr, idx):
    result = [i[0] for i in list(enumerate(arr))[idx:] if i[1] == 1]
    return result[0] if len(result) !=0 else -1
