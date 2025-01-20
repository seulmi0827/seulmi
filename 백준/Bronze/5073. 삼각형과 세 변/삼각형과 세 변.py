result = []
while True:
    i = input()
    if i != '0 0 0':
        result.append(i)
        continue
    else:
        break
for tri in result:
    a,b,c = map(int,tri.split())
    if max([a,b,c])*2 >= sum([a,b,c]):
        print('Invalid')
    else:
        if a == b == c:
            print('Equilateral')
        elif a==b or b==c or a==c:
            print('Isosceles')
        else:
            print('Scalene')