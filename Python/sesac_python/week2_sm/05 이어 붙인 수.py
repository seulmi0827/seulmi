def solution(num_list):
    list_ = []
    list2_=[]
    for num in num_list:
        if num%2 == 1:
            list_.append(str(num))
            odd = "".join(list_)
        else:
            list2_.append(str(num))
            even = "".join(list2_)
    return int(odd)+int(even)
