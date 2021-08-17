# 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/look-and-say-sequence/description
n = int(input())

arr = [[] for _ in range(n + 1)]
	
arr[1].append(1)

for i in range(1, n):
    cnt = 1
    for j in range(1, len(arr[i]) + 1):
        if j == len(arr[i]) or arr[i][j] != arr[i][j - 1]:
            arr[i + 1].append(arr[i][j - 1])
            arr[i + 1].append(cnt)
            cnt = 1
        else:
            cnt += 1
for i in arr[n]:
    print(i,end='')