# 1. Basic
# 단순 반복문 - 완전수
# 완전수란 자기 자신을 제외한 모든 양의 약수들을 더했을 때 자기 자신이 되는 수 입니다.
# 주어지는 start에서 end 이내에 있는 숫자들 중 완전수가 몇 개인지 출력하는 코드를 작성해보세요.
# 출처 : 코딩테스트 준비를 위한 알고리즘 정석
# https://www.codetree.ai/missions/2/concepts/1/problems/perfect-number/description
start, end = map(int,input().split())
count = 0
for i in range(start, end+1):
    res = 0
    for j in range(1, i):
        if i%j == 0:
            res += j
    if res == i:
        count += 1
print(count)