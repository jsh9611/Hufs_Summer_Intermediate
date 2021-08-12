# 1. Basic 
# 객체 정렬 - 줄 세우기
# 규칙에 따라 정렬한 이후의 결과를 N개의 줄에 걸쳐 출력합니다. 
# 각 줄에는 정렬한 이후 N명의 학생의 정보를 순서대로 한 줄에 하나씩 출력합니다. 
# 각 줄에는 각 학생의 키, 몸무게, 그리고 번호를 공백을 사이에 두고 출력합니다.
# 출처 : https://www.codetree.ai/missions/2/concepts/1/problems/line-up-students/introduction
n = int(input())
info = []
for i in range(1,n+1):
    h,w = map(int, input().split())
    info.append([h,w,i])
info.sort(key = lambda x: (-x[0], -x[1]))
for i in range(n):
    print(*info[i])