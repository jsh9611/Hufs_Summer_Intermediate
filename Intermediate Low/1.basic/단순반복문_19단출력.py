# 1. Basic 
# 단순반복문 - 19단 출력
# 각 문자 간에 공백을 두고 위의 양식에 맞추어 출력합니다.
# 출처 : https://www.codetree.ai/missions/2/concepts/1/problems/nineteen-times-table/description
for i in range(1,20):
    for j in range(1,20):
        if j==19:
            print(f'{i} * {j} = {i*j}')
        elif j%2 == 1:
            print(f'{i} * {j} = {i*j} / ', end='')
        else:
            print(f'{i} * {j} = {i*j}')