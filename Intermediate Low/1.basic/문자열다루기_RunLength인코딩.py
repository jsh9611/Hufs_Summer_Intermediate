s = input()

temp = s[0]
count = 0
ans = ''
for item in s:
    if item == temp:
        count += 1
    else:
        ans += temp + str(count)
        temp = item
        count = 1
ans += temp + str(count)

print(len(ans))
print(ans)