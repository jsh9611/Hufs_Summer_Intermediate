n = int(input())
arr = list(map(int,input().split()))

left = arr[0]
right = arr[0]
income = 0

for item in arr:
    if item < left:
        left = item
        right = item
    elif item>right:
        right = item
    if right - left > income:
        income = right - left
print(income)

# 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/max-profit-of-single-car/description