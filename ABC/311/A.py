n = int(input())
s = input()

found_a = False
found_b = False
found_c = False
result = -1  # 条件を満たす位置が見つからない場合のデフォルト値

for num, char in enumerate(s):
    if char == 'A':
        found_a = True
    elif char == 'B':
        found_b = True
    elif char == 'C':
        found_c = True
    
    if found_a and found_b and found_c:
        result = num + 1  # インデックスは 0 から始まるため +1 をして設定
        break

print(result)