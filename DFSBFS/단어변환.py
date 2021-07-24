# 2021.07.24. 2021 DFS & BFS(Programmers High score kit)
# 단어 변환

'''
<풀이 아이디어>
1) 단어에서 글자를 하나씩 바꾸면서 변환 가능한 단어를 탐색하는 DFS
'''

import sys


def solution(begin, target, words):
    answer = sys.maxsize
    N = len(begin)

    def dfs(start):             # DFS
        discovered = []
        stack = [start]
        while stack:
            v = stack.pop()
            if v == target:             # 타겟에 도착하면 종료시키고 경로를 반환
                break
            if v not in discovered:     # 방문하지 않은 점이면 단어를 변환
                discovered.append(v)
                for word in words:
                    if word not in discovered:
                        for i in range(N):
                            if v[:i]+v[i+1:] == word[:i]+word[i+1:]:
                                stack.append(word)
        return discovered

    if target not in words:         # 예외 처리
        return 0
    else:
        for word in words:
            for i in range(N):
                if word[:i]+word[i+1:] == begin[:i]+begin[i+1:]:
                    answer = min(answer, len(dfs(word))+1)
        return answer
