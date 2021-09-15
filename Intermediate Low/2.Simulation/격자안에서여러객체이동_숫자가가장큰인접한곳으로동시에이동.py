# 2. Simulation
# 격자 안에서 여러 객체를 이동 - 숫자가 가장 큰 인접한 곳으로 동시에 이동
# 1 ~ 100 사이의 숫자로 이루어진 n * n 크기의 격자판 정보가 주어집니다. 
# 이때 m개 구슬이 서로 다른 위치에서 시작하여 1초에 한 번씩 상하좌우로 인접한 곳에 
# 있는 숫자들 중 가장 큰 값이 적혀있는 숫자가 있는 위치로 동시에 이동합니다.
# 출처 : 코드트리 - 코딩테스트 준비를 위한 알고리즘 정석
# https://www.codetree.ai/missions/2/concepts/2/problems/move-to-max-adjacent-cell-simultaneously/description
# 변수 선언 및 입력
n, m, t = map(int, input().split())

a = [[0]*(n+1) for _ in range(n + 1)]
count = [[0]*(n+1) for _ in range(n + 1)]
next_count = [[0]*(n+1) for _ in range(n + 1)]

# 범위가 격자 안에 들어가는지 확인
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

# 인접한 곳들 중 가장 값이 큰 위치를 반환
def get_max_neighbor_pos(curr_x, curr_y):

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    max_num = 0
    max_pos = (0, 0)
    
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
            max_pos = (next_x, next_y)
    
    return max_pos

def move(x, y):
    next_x, next_y = get_max_neighbor_pos(x, y)
    next_count[next_x][next_y] += 1

def move_all():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            next_count[i][j] = 0
            
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] == 1:
                move(i, j)
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[i][j] = next_count[i][j]

def remove_duplicate_marbles():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] >= 2:
                count[i][j] = 0

def simulate():
    move_all()
    remove_duplicate_marbles()

for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem
        
for _ in range(m):
    x, y = map(int, input().split())
    count[x][y] = 1
    
for _ in range(t):
    simulate()

print(sum(count[i][j] 
    for i in range(1,n+1) 
    for j in range(1,n+1)))