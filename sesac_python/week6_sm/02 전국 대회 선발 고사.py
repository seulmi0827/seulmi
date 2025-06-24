def solution(rank, attendance):
    result = list(zip(rank,attendance))
    result2 = sorted([(result[i][0],i) for i in range(len(result)) if result[i][1]==True])[:3]
    a,b,c = [i[1] for i in result2]
    return 10000*a + 100*b + c
