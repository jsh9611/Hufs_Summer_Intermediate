# 1. Basic
# 문자열 다루기 - 문자열 한 칸씩 밀어내며 뒤집기
# 가장 앞에 있는 문자를 제외한 나머지 문자를 한 칸씩 앞으로 당기고 가장 앞에 있던 문자를 가장 뒤로 옮깁니다.
# 가장 뒤에 있는 문자를 제외한 나머지 문자를 한 칸씩 뒤로 밀고 가장 뒤에 있던 문자를 가장 앞으로 옮깁니다.
# 문자열을 좌우로 뒤집습니다.
# 출처 : https://www.codetree.ai/missions/2/concepts/1/problems/shift-reverse-string/description
a, b = input().split()

for i in range(int(b)):
    option = int(input())
    if option == 1:
        a = a[1:] + a[0]
        print(a)
    elif option == 2:
        a = a[-1] + a[:-1]
        print(a)
    elif option == 3:
        a = a[::-1]
        print(a)