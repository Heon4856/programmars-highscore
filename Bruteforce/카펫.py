# 2021.07.24. 2021 Bruteforce(Programmers High score kit)
# 카펫

'''
<풀이 아이디어>
1) 이건 그리디 아닌가? Ez
'''


def solution(brown, yellow):
    row_col = (brown - 4)//2
    answer = []
    for i in range(row_col-1, 1-1, -1):
        if i * (row_col-i) == yellow:
            answer.append(i+2)
            answer.append(row_col-i+2)
            break
    return answer
