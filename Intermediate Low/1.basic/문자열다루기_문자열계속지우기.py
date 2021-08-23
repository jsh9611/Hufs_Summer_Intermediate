a = input()
b = input()

len_b = len(b)

while b in a:
    ans = a.index(b)
    a = a[:ans] + a[ans+len_b:]
print(a)

# 문자열 계속 지우기
# 문제 출처: 코드트리
# https://www.codetree.ai/missions/2/concepts/1/problems/keep-removing-string/description