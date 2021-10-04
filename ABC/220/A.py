a, b, c = int(input().split())

multiple = range(((a - 1) // c + 1) * c, b, c)

if not multiple:
    print(-1)
elif a <= multiple[0] <= b:
    print(multiple[0])
