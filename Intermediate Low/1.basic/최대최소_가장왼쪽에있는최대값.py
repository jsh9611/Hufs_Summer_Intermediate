n = int(input())
arr = list(map(int,input().split()))

def find_max(a):
    max = -1
    for item in a:
        if item > max:
            max = item
    return max

max_index = arr.index(find_max(arr))

print(max_index+1,end=' ')

while max_index != 0:
    max_index = arr.index(find_max(arr[:max_index]))
    print(max_index+1,end=' ')3

# 문제출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/leftmost-max-value/description