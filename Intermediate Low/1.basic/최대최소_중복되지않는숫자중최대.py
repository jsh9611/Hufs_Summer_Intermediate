n = int(input())
arr = list(map(int,input().split()))

ans = [0]*1001
for item in arr:
    ans[item] += 1

for i in range(1000,-1,-1):
    if ans[i] == 1:
        print(i)
        break
    if i == 0:
        print(-1)

# 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/max-of-unique-number/description