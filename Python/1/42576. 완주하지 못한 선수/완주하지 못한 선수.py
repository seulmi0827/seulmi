from collections import defaultdict
def solution(participant, completion):
    result = defaultdict(int)
    for i in participant:
        result[i] +=1
    for j in completion:
        result[j] -= 1
    for k in result:
        if result[k] == 1:
            return k