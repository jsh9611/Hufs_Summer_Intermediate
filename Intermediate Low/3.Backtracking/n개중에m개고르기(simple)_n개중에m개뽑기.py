# n개중에m개고르기(simple)_n개중에m개뽑기.py
# https://www.codetree.ai/missions/2/concepts/3/problems/n-choose-m/introduction
# 변수 선언 및 입력
n, m = map(int, input().split())
combination = []

def find_combination(num, cnt):
    if num == n+1:
        if cnt == m:
            for item in combination:
                print(item, end = ' ')
            print()
        return

    combination.append(num)
    find_combination(num+1, cnt+1)
    combination.pop()

    find_combination(num+1, cnt)

find_combination(1,0)