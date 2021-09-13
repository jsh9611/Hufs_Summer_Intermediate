def shift():
    n = len(s)
    temp = s[n-1]
    for i in range(n-1):
        s[n-1-i] = s[n-2-i]
    s[0] = temp

def find_len(lists):
    temp = lists[0]
    count = 0
    s = ''
    for item in lists:
        if item == temp:
            count += 1
        else:
            s += temp + str(count)
            temp = item
            count = 1
    s += temp + str(count)
    return len(s)

s = list(input())
min_len = find_len(s)

for i in range(len(s)-1):
    shift()
    min_len = min(min_len,find_len(s))

print(min_len)
# 문제출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/2/problems/shortest-run-length-encoding/submissions