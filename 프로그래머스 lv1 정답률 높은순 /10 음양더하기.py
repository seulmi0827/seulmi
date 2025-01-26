def solution(absolutes, signs):
    return sum([absolutes[i]*1 if signs[i]== True else absolutes[i]*-1 for i in range((len(signs)))])
