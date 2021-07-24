# 2021.07.24. 2021 DFS & BFS(Programmers High score kit)
# 타겟 넘버

'''
<풀이 아이디어>
1) DFS로 하나씩 쭈욱~
'''


def solution(numbers, target):

    def dfs(index, operation, result):
        if index == N-1:
            if operation == "+":
                result += numbers[index]
            elif operation == "-":
                result -= numbers[index]

            if result == target:
                answer.append(1)
                return
            return

        else:
            if operation == "+":
                result += numbers[index]
            elif operation == "-":
                result -= numbers[index]

            dfs(index+1, "+", result)
            dfs(index+1, "-", result)

    N = len(numbers)
    answer = []

    dfs(0, "+", 0)
    dfs(0, "-", 0)

    return len(answer)
