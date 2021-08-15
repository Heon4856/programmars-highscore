# 2021.07.31. 2021 DFS & BFS (Baekjoon 2178)
# 미로 탐색

'''
<풀이 아이디어>
1) BFS로 4방향 중 갈 수 있는 길을 선택하여 간다.
2) 방문 지점을 표시하여 먼저 도착한 길은 또 가지 않는다.
'''

import sys
from collections import deque
read = sys.stdin.readline().rstrip()


N, M = map(int, read().split())
# 지도
matrix = [list(read()) for _ in range(N)]
# 방문 지점
discovered = [[0]*M for _ in range(N)]
# 동서남북
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]


def BFS(i, j):
    discovered[j][i] = 1
    # using Deque
    Q = deque([(i, j)])
    while Q:
        x, y = Q.popleft()
        # ending point
        if x == N-1 and y == M-1:
            break
        # moving in 4-direction
        for i in range(4):
            if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N and \
                    discovered[y+dy[i]][x+dx[i]] == 0 and\
                    matrix[y+dy[i]][x+dx[i]] == '1':
                # marking distance in discovered
                discovered[y+dy[i]][x+dx[i]] = discovered[y][x]+1
                Q.append([x+dx[i], y+dy[i]])
    return discovered
    # return end-point


print(BFS(matrix))
