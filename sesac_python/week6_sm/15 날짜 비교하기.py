def solution(date1, date2):
    date1 = [str(i) for i in date1]
    date2 = [str(i) for i in date2]
    return int(int(''.join(date1)) < int(''.join(date2)))

##다른사람풀이
def solution(date1, date2):
    return int(date1 < date2) #리스트간 부등호 사용가능
