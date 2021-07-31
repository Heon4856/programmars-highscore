# 2021.07.31. 2021 DFS & BFS (Baekjoon 1260)
# DFS와 BFS

'''
<풀이 아이디어>
1) 그냥 뭐.. dfs는 재귀랑 스택, bfs는 큐로 구현
'''

from collections import defaultdict

graph = defaultdict(list)

N, M, V = map(int, input().split())
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

discovered = []


def dfs_recur(v):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            dfs_recur(w)
    return


dfs_recur(V)


def dfs_stack(v):
    discovered = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in sorted(graph[v], reverse=True):
                stack.append(w)
    return discovered


def bfs(v):
    discovered = []
    stack = [v]
    while stack:
        v = stack.pop(0)
        if v not in discovered:
            discovered.append(v)
            for w in sorted(graph[v]):
                stack.append(w)
    return discovered


# print(*discovered)
print(*dfs_stack(V))
print(*bfs(V))
