# 1. Basic 
# 일반정렬 - Top k 숫자 구하기
# 오름차순으로 정렬했을 때 k번째 숫자를 출력합니다.
# 출처 : https://www.codetree.ai/missions/2/concepts/1/problems/kth-number/description
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
print(a[m-1])