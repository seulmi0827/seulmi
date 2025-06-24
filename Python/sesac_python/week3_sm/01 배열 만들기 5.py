def solution(intStrs, k, s, l):
        return [int(total[s:s+l]) for total in intStrs if int(total[s:s+l])>k]
