# 1. Basic
# 단순 반복문 - 약수의 개수가 3개인 수
# 주어지는 두 수(start, end)에 대해서, start 이상, end 이하의 숫자 중에
# 약수가 3개인 숫자의 개수를 구하는 코드를 작성해보세요.
# 출처 : 코딩테스트 준비를 위한 알고리즘 정석
# https://www.codetree.ai/missions/2/concepts/1/problems/square-of-prime-number/description
start, end = map(int,input().split())
count = 0
for i in range(start, end+1):
    divisor_count = 0
    for j in range(1, i+1):
        if i%j == 0:
            divisor_count += 1
    if divisor_count == 3:
        count += 1
print(count)