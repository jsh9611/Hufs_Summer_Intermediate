n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
answer = 0
for i in range(n):
    temp = -1
    for j in range(n):
        if temp == arr[i][j]:
            count += 1
        else:
            temp = arr[i][j]
            count = 1
        if count == m:
            answer += 1
            break

for j in range(n):
    temp = -1
    for i in range(n):
        if temp == arr[i][j]:
            count += 1
        else:
            temp = arr[i][j]
            count = 1
        if count == m:
            answer += 1
            break
print(answer)
# 문제출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/2/problems/number-of-happy-sequence/description