import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

ans = 0

# tromino 비교하기
# ㄴ 모양
dx = [-1,-1,0,0]
dy = [-1,0,-1,0]
for i in range(1,n):
    for j in range(1,m):
        sum = arr[i-1][j-1] + arr[i-1][j]\
            + arr[i][j-1]+arr[i][j]
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            ans = max(ans,(sum - arr[nx][ny]))
# 세로모양
for i in range(2,n):
    for j in range(m):
        ans = max(ans,(arr[i][j]+arr[i-1][j]+arr[i-2][j]))
# 가로모양
for i in range(n):
    for j in range(2,m):
        ans = max(ans,(arr[i][j]+arr[i][j-1]+arr[i][j-2]))

# 출력
print(ans)

# 코드트리 - 트로미노
# https://www.codetree.ai/missions/2/concepts/2/problems/tromino/submissions