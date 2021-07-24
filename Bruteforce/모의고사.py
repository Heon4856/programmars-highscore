# 2021.07.19. 2021 Bruteforce(Programmers High score kit) 
# 모의고사

'''
<풀이 아이디어>
1) 찍는 방식은 고정되어 있다.
    - 리스트를 만들자.
'''

import collections
def solution(answers):
    ans_dict = collections.defaultdict(int)
    N = len(answers)
    for i,v in enumerate(answers):
        ans_dict[i+1]=v
    ans_1 = [i for i in range(1,5+1)] * (N//5) +[i for i in range(1,N%5 +1)]
    ans_2 = [2,1,2,3,2,4,2,5]*(N//8) + [2,1,2,3,2,4,2,5][0:(N%8)]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]*(N//10) + [3,3,1,1,2,2,4,4,5,5][0:(N%10)]
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    for i in range(N,1-1,-1):
        ans = ans_dict[i]
        if ans_1.pop() == ans:
            score_1 += 1
        if ans_2.pop() == ans:
            score_2 += 1
        if ans_3.pop() == ans:
            score_3 += 1
    answer = []
    M = max(score_1,score_2,score_3)
    if score_1 == M:
        answer.append(1)
    if score_2 == M:
        answer.append(2)
    if score_3 == M:
        answer.append(3)
        
    return answer