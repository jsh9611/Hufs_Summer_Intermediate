import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def find_ans(i,j,a,b):
    # 대각선 방향
    dx = [-1,-1,1,1]
    dy = [1,-1,-1,1]
    # 마름모 길이        # /\
    rhomb = [a,b,a,b]   # \/
    x,y = i,j
    result = 0

    # 네 방향을 순회
    for d in range(4):
        # 각 방향에 해당하는 길이만큼 이동
        for _ in range(rhomb[d]):
            x = x + dx[d]
            y = y + dy[d]

            # 범위 밖이면 0을 return
            if x<0 or y<0 or x>=n or y>=n:
                return 0
            
            result += arr[x][y]
    return result

ans = 0
for i in range(n): # 행
    for j in range(n): # 열
        for a in range(1,n): # 대각선 / 길이(정사영)
            for b in range(1,n): # 대각선 \ 길이(정사영)
                ans = max(ans, find_ans(i,j,a,b))
print(ans)
# 문제 - 코드트리
# https://www.codetree.ai/missions/2/concepts/2/problems/slanted-rectangle/description