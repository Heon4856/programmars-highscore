# 2021.07.24. 2021 DFS & BFS(Programmers High score kit)
# 여행 경로

'''
<풀이 아이디어>
1) 주어진 항공권을 모두 사용하라?
'''

from collections import defaultdict


def solution(tickets):
    tickets.sort(reverse=True)          # 알파벳 역순으로 정렬
    routes = defaultdict(list)
    for t1, t2 in tickets:
        routes[t1].append(t2)

    stack = ['ICN']
    ans = []
    while stack:
        v = stack[-1]
        # 다음 경로가 없거나 경로의 끝에 온 경우
        if v not in routes or len(routes[v]) == 0:
            ans.append(stack.pop())
        else:                                           # 다음 경로를 추가
            stack.append(routes[v].pop())
    ans.reverse()       # 다시 원래 순서로 되돌려 리턴
    return ans
