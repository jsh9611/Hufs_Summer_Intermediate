a = input()
len_a = len(a)

b = input()
a = a+b
ans = a.index(b)

if len_a == ans:
    print(-1)
else:
    print(ans)
    
# 부분문자열 위치 구하기
# 문제 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/find-location-of-substring/solution