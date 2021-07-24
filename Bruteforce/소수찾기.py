# 2021.07.24. 2021 Bruteforce(Programmers High score kit)
# 소수 찾기

'''
<풀이 아이디어>
1) 흩어진 종이 조각을 붙여?
    - 조합을 이용하자
2) 에라토스테네스의 체를 이용해서 소수를 찾자
3) DP를 이용해 조금 더 최적화를 할 수 있지만 다음 기회에~
'''

from itertools import permutations
from collections import defaultdict


def solution(numbers):
    answer = 0
    list_num = list(numbers)    # ['0','1','7']
    discovered = []

    def isPrimeNum(num):
        if num == 0 or num == 1:       # 에라토스테네스의 체
            return 0
        elif num == 2 or num == 3:
            return 1
        elif num > 3:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return 0
            else:
                return 1
        return 0

    for k in range(1, len(numbers)+1):       # 조합으로 고를 가지 수 k개
        for c in permutations(list_num, k):  # 숫자를 k개 뽑는 경우들
            num = int(''.join(c))
            if num not in discovered:
                answer += isPrimeNum(num)
                discovered.append(num)

    return answer


print(solution("3"))
