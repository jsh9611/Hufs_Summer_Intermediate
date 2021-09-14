def tri_belt(arr,n,t):
    for _ in range(t):
        temp1 = arr[0][n-1]
        temp2 = arr[1][n-1]
        temp3 = arr[2][n-1]
        for i in range(n-1):
            arr[0][n-1-i] = arr[0][n-2-i]
            arr[1][n-1-i] = arr[1][n-2-i]
            arr[2][n-1-i] = arr[2][n-2-i]
        arr[0][0] = temp3
        arr[1][0] = temp1
        arr[2][0] = temp2

n,t = map(int,input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int,input().split())))

tri_belt(arr,n,t)

for i in range(3):
    print(*arr[i])
# 문제 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/2/problems/conveyor-belt-triangle/description