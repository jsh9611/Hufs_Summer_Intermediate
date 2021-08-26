import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [[0]*m for _ in range(n)]

count = 1
now = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            row = i
            col = j
            while 0 <= col and row < n:
                arr[row][col] = count
                row += 1
                col -= 1
                count += 1

for i in range(n):
    print(*arr[i]) 

# 출처 : 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/diagonal-numbering/description
