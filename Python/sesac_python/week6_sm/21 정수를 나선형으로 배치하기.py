def solution(n): 
    zeros = [[0 for i in range(n)] for j in range(n)]
    i = 0
    k = 0
    while True:
        while i <n:
            for j in range(0,n):
                zeros[0][j] = i -n + 7
                i+=1
        while n*1 <= i < n*2:
            for j in range(1,n):
                zeros[j][n-1] = i-n+2
                i+=1
        while n*2<=i < n*3:
            for j in range(-2,-n-1,-1):
                zeros[-1][j] = i-n+2
                i+=1
        while n*3<=i < n*4:
            for j in range(-2,-n,-1):
                zeros[j][0] = i-n+2
                i+=1
        while n*4<=i < n*5:
            for j in range(1,n-1):
                zeros[1][j] = i-n-2
                i+=1
        while n*5 <= i < n*6:
            for j in range(2,n-1):
                zeros[j][n-2] = i-n-2
                i+=1
        while n*6 <= i < n*7:
            for j in range(-3,-n,-1):
                zeros[-2][j] = i-n-5
                i+=1
        break
