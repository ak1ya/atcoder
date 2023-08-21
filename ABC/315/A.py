S = input()
remove = "aeiou"
result = S
for i in remove:
    result = result.replace(i, "")
print(result)
