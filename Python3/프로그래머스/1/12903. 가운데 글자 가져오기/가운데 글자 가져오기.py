def solution(s):
    if len(s)%2==1:
        return s[int((len(s)-len(s)%2)/2)]
    else:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]