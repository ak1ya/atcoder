contests = ["ABC","ARC","AGC","AHC"]
s1 = input()
s2 = input()
s3 = input()

if s1 in contests:
    contests.remove(s1)
    if s2 in contests:
        contests.remove(s2)
        if s3 in contests:
            contests.remove(s3)

print(contests[0])
