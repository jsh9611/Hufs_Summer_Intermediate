n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([abs(a)+abs(b),i])
arr.sort()
for item in arr:
    print(item[1]+1)

# 문제출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/distance-from-origin/submissions