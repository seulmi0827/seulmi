n = int(input())
result = []
for _ in range(n):
    i = input()
    result.append(i)
start = result[0]
for i in result[1:]:
    start = ''.join([j if j == start[idx] else '?' for idx, j in enumerate(i)])
print(start)