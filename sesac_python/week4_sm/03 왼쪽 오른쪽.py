def solution(str_list):
    uldict = {"l":0,"r":0}
    for i in range(len(str_list)):
        if str_list[i] in uldict:
            uldict[str_list[i]]+=1
            if uldict["l"] == 1: return str_list[:i]
            elif uldict["r"] == 1: return str_list[i+1:]
    return []
