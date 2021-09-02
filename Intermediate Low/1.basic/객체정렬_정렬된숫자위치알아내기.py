n = int(input())
arr = list(map(int,input().split()))
ans = [0]*n
arr2 = []
for i,num in enumerate(arr):
    arr2.append([num,i])
arr2.sort()
for i, number in enumerate(arr2):
    ans[number[1]] = i + 1
print(*ans)
# 문제출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/indices-of-sorted-array/description