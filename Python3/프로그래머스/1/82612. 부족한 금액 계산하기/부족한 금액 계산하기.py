def solution(price, money, count):
    result = money - sum([price*num for num in range(count+1)])
    return 0 if result > 0 else abs(result)


        