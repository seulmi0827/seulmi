def solution(a, b, included):
    list_1 = [i for i in range(a,100000,b)][:len(included)]
    dict_1 = dict(zip(list_1,included))
    print(list_1)
    
    keys_sum=0
    for keys in list_1:
        if dict_1[keys]:
            keys_sum += keys
    return keys_sum
