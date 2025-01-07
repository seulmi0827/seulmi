def solution(n):
    for i in range(1,n+1) :
        if n%i == 1:
            return i

def soulution(n):
  return min([i for i in range(1,1000000) if n%i==1])
