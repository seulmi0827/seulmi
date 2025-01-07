def solution(s):
    p_list = [p for p in s.lower() if p == 'p']
    y_list = [y for y in s.lower() if y == 'y']
    return len(p_list)==len(y_list)
