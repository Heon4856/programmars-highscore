# 2021.07.24. 2021 DFS & BFS(Programmers High score kit)
# 네트워크

'''
<풀이 아이디어>
1) 네트워크를 모두 돌고 나오면 하나의 네트워크!
'''


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    def dfs(com):
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:  # 연결된 컴퓨터
                if not visited[connect]:
                    dfs(connect)

    for com in range(n):
        if not visited[com]:
            dfs(com)
            answer += 1  # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer
