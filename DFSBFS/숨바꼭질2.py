# 2021.07.25. 2021 DFS & BFS (Baekjoon)
# 숨바꼭질 2

'''
<풀이 아이디어>
1) x+1, x-1, 2*x의 이동을 할 수 있다.
    - DFS로 찾을까도 생각을 했지만 DFS로 할시 가장 먼저 도착하는 경우와 방법의 수를 찾을 수가 없다.
2) BFS로 할때 주의점
    - BFS는 무조건 방문경로를 표시해줘야한다. 방문 표시가 없으면 3의 제곱으로 무한히 늘어나므로 메모리 부족이 야기된다.
'''

from collections import deque
MAX_SIZE = 100000


def bfs(start, end):
    Q = deque()
    Q.append([start, 0])
    method = []
    visited = [0 for _ in range(MAX_SIZE+1)]
    while Q:
        v, cnt = Q.popleft()
        visited[v] = cnt
        if method and method[0] < cnt:
            continue

        elif v == end:
            method.append(cnt)
            continue

        for dv in [v*2, v+1, v-1]:
            if 0 <= dv <= MAX_SIZE:
                if not visited[dv] or visited[dv] >= cnt+1:
                    Q.append([dv, cnt+1])
                    visited[dv] = cnt+1

    return method[-1], len(method)


N, K = map(int, input().split())

print(*bfs(N, K), sep='\n')
