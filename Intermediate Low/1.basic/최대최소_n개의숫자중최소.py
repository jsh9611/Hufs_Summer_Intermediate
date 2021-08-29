# 1. Basic 
# 최대 최소 - n개의 숫자 중 최소
# 최솟값과 그 값에 해당하는 원소의 개수를 공백을 사이에 두고 출력합니다.
# 출처 : https://www.codetree.ai/missions/2/concepts/1/problems/min-of-n-num/description
n = int(input())
list = list(map(int,input().split()))
list.sort()

count = 0
for item in list:
    if item == list[0]:
        count += 1
    else:
        break
print(list[0], count)

# cnt 변수를 사용해서 for문 하나로 풀 수 있다
# min이 동일한 경우 cnt를 1 증가
# min = list[0]
# cnt = 1