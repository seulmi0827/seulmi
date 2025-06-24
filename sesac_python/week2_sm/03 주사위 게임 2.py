def solution(a, b, c):
    if a==b==c:
        return (a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c)
    elif a==b or b==c or a==c:
        return (a+b+c)*(a*a+b*b+c*c)
    elif a!=b and b!=c and c!=a:
        return a+b+c
