# 2. Simulation
# 격자 안에서 밀고 당기기 - 컨베이어 벨트
# t초의 시간이 흐른 뒤 컨베이어 벨트에 놓여있는 
# 숫자들의 상태를 출력하는 프로그램을 작성해보세요.
# 출처 : 코드트리 - 코딩테스트 준비를 위한 알고리즘 정석
# https://www.codetree.ai/missions/2/concepts/2/problems/conveyor-belt/description
n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(t):
    temp = u[-1]
    
    # 벨트의 위에 부분 계산
    for i in range(n-1, 0, -1):
        u[i] = u[i-1]
    u[0] = d[-1]
    
    # 벨트의 아랫 부분 계산
    for i in range(n-1, 0, -1):
        d[i] = d[i-1]
    d[0] = temp

for item in u:
    print(item, end=" ")
print()

for item in d:
    print(item, end=" ")
print()