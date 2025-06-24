def solution(arr):
    row_n = len(arr)
    column_n = len(arr[0])
    while row_n < column_n:
            arr.append([0]*column_n)
            row_n = len(arr)
    while row_n > column_n:
        for i in arr:
            i.append(0)
            column_n = len(arr[0])
    return arr
