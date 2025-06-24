def solution(code):
    ret = ''
    mode = 0
    idx = 0
    while idx < len(code):
        for i in code:
            if mode == 0:
                if code[idx] == '1':
                    mode = 1
                    idx += 1
                elif idx % 2==0:
                    ret += i
                    idx += 1
                else:
                    idx +=1
            elif mode == 1:
                if code[idx] == '1':
                    mode = 0
                    idx += 1
                elif idx % 2==1:
                    ret += i
                    idx +=1
                else:
                    idx +=1
    return ret if len(ret)>0 else "EMPTY"
