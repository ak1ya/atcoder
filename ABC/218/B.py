p = list(map(int, input().split()))

s = ''
for i in range(26):
    s = s+chr(p[i]+96)

print(s)
