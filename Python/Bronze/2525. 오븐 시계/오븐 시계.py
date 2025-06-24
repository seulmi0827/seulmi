h, m = map(int,input().split())
time = int(input())

time_h = int((time-(time % 60))/60)
time_m = time % 60

result_h = h + time_h

result_m = m + time_m
if result_m >= 60:
    result_m -=60
    result_h +=1

if result_h >= 24:
    result_h -= 24
    
print(result_h,result_m)