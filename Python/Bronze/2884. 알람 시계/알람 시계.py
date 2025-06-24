h, m = map(int,input().split())
m_re = m - 45
if m_re < 0:
    m_re += 60
    h -= 1
    if h <0:
        h +=24
print(h,m_re)