n = int(input())
arr = list(map(int,input().split()))

arr.sort()

answer = 0
for i in range(n):
    answer = max(answer, arr[0+i]+arr[2*n-1-i])
print(answer)
# 문제출처 : 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/group-of-pairs/solution