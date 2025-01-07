def solution(s):
    try:
        return int(s)
    except Exception:
        return (-1)*int(s[1:])
