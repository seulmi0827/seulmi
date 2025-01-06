def solution(n):
    return 0 if n==0 else sum([i for i in range(1,3001) if n % i == 0])
