import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = n
arr = [[0]*m for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def fill_box(x, y):
    i = 0
    count = 2
    arr[x][y] = 1
    for _ in range(n*m*2):
        i = i%4
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            i = i+1
            continue

        if arr[nx][ny] > 0 and count > arr[nx][ny]:
            i -= 1
            continue
        else:
            arr[nx][ny] = count
            count += 1
            x = nx
            y = ny
            i += 1
fill_box(n//2,m//2)

for i in range(n):
    print(*arr[i])

# 출처 : 코드트리 - 가운데에서 시작하여 빙빙 돌기
# https://www.codetree.ai/missions/2/concepts/1/problems/snail-start-from-center/description