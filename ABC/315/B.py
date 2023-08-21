M = int(input())
D = list(map(int,input().split()))
ans = (sum(D)+1)//2

for i in range(M):
    if D[i] < ans:
        ans -= D[i]
    else:
        print(i+1, ans)
        exit()

