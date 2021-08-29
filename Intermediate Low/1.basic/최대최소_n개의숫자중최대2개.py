n = int(input())
arr = list(map(int,input().split()))

arr.sort()

print(arr[n-1], arr[n-2])

# 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/two-max-of-n-num/description