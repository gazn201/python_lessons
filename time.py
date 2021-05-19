h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
H = ((h1-h2)*(60**2))
M = ((m1-m2)*60)
S = (s1-s2)
print(abs(H+M+S))


