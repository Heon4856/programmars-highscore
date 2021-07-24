import math
import itertools


# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers):
    numbers = list(numbers)
    List = []
    ans_temp = []
    for i in range(1, len(numbers) + 1):
        temp = itertools.permutations(numbers, i)
        List += temp
        for j in List:
            temp2 = ""
            for k in j:
                temp2 += k
                if is_prime_number(int(temp2)):
                    ans_temp.append(int(temp2))

    ans = set(ans_temp)

    print(ans)

    answer = len(ans)

    return answer

