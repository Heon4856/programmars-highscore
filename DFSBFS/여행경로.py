# 2021.07.24. 2021 DFS & BFS(Programmers High score kit)
# 여행 경로

'''
<풀이 아이디어>
1) 주어진 항공권을 모두 사용하라?
'''


def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    stack = ['ICN']
    ans = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            ans.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    ans.reverse()
    return ans
