n = input().lower()
result = dict()
score = 0
for i in list(set(n)):
    result[i] = 0
    
for j in n:
    result[j] += 1
    
for k in result :
    if result[k] == max(result.values()):
        score += 1
        answer = k
if score == 1:
    print(answer.upper())
else:
    print('?')