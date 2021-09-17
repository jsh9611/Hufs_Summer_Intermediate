# k중1개n번선택(conditional)-특정조건에맞게k중1개n번뽑기.py


# https://www.codetree.ai/missions/2/concepts/3/problems/n-permutations-of-k-with-repetition-under-constraint/description
k, n = map(int,input().split())
selected = []
visited = [False]*k

def find_combination(curr, cnt):
    if cnt == n:
        print(*selected)
        return
    
    for i in range(1,n+1):
        visited[i] = True
        find_combination(1,i)
        visited[i] = False


for i in range(1,n+1):
    visited[i] = True
    find_combination(1,i)
    visited[i] = False