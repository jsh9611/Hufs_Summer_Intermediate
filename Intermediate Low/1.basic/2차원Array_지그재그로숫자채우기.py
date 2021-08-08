# 1. Basic 
# 2차원 array - 지그재그로 숫자 채우기
# 숫자로 채워진 완성된 형태의 n * m 크기의 사각형을 출력합니다. 
# (숫자끼리는 공백을 사이에 두고 출력합니다.)
# 출처 : https://www.codetree.ai/missions/2/concepts/1/problems/zigzag-numbering/description
n,m = map(int,input().split())
arr = [[0]*m for _ in range(n)]

start = 0
for i in range(m):
    if i%2 == 1:
        for j in range(n-1,-1,-1):
            arr[j][i] = start
            start += 1
    else:
        for j in range(n):
            arr[j][i] = start
            start += 1

for i in range(n):
    print(*arr[i])