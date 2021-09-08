# 2. Simulation
# 격자 안에서 달일 객체를 이동 - 숫자가 더 큰 인접한 곳으로 이동
# 1 ~ 100 사이의 숫자로 이루어진 n * n 크기의 격자판 정보가 주어집니다. 
# 방문하게 되는 위치에 적힌 숫자를 순서대로 출력하는 프로그램을 작성해보세요.
# 출처 : 코드트리 - 코딩테스트 준비를 위한 알고리즘 정석
# https://www.codetree.ai/missions/2/concepts/2/problems/move-to-larger-adjacent-cell/description
n, nx, ny = map(int, input().split())

a = [[0]*(n+1) for _ in range(n+1)]

visited = []

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def can_go(x, y, num):
    return in_range(x, y) and a[x][y] > num

# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인
# 움직일 수 있다면 true를 움직일 수 없다면 false를 return
def simulate():
    global nx, ny
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인
    for dx, dy in zip(dx, dy):
        next_x, next_y = nx + dx, ny + dy
        
        # 갈 수 있는 곳이라면 이동하고 true를 반환
        if can_go(next_x, next_y, a[nx][ny]):
            nx, ny = next_x, next_y
            return True
    
    # 움직일 수 있는 곳이 없으면 false
    return False

for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    for j, item in enumerate(given_row, start = 1):
        a[i][j] = item

# 처음에 방문한 곳을 저장한다
visited.append(a[nx][ny])

while True:
    greater_number_exist = simulate()

    # 인접한 곳에 더 큰 숫자가 없다면 종료
    if not greater_number_exist:
        break
    
    # 움직이고 난 후의 위치를 저장한다
    visited.append(a[nx][ny])

for num in visited:
    print(num, end=' ')