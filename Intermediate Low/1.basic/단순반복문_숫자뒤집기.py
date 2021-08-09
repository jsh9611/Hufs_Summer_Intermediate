# 1. Basic
# 단순 반복문 - 숫자 뒤집기
# 자연수가 입력으로 주어질 때 해당 자연수를 일의 자리부터 
# 거꾸로 출력하는 코드를 작성해보세요. (ex : 1234 → 4321)
# 출처 : 코딩테스트 준비를 위한 알고리즘 정석
# https://www.codetree.ai/missions/2/concepts/1/problems/square-of-prime-number/description
num = input()
for i in range(len(num)-1,-1,-1):
    if num[i] == '0':
        continue
    print(num[i::-1])
    break