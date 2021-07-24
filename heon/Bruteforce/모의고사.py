
def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num1 = 5
    num2 = 8
    num3 = 10

    ans_num = len(answers)

    supo1_ans = supo1 * (ans_num // num1) + supo1[:ans_num % num1]
    supo2_ans = supo2 * (ans_num // num2) + supo2[:ans_num % num2]
    supo3_ans = supo3 * (ans_num // num3) + supo3[:ans_num % num3]

    correct_1 = 0
    correct_2 = 0
    correct_3 = 0

    for i in range(ans_num):
        answer_i = answers[i]

        if supo1_ans[i] == answer_i:
            correct_1 += 1
        if supo2_ans[i] == answer_i:
            correct_2 += 1
        if supo3_ans[i] == answer_i:
            correct_3 += 1

    ans = max(correct_1, correct_2, correct_3)

    if ans == correct_1:
        answer.append(1)
    if ans == correct_2:
        answer.append(2)
    if ans == correct_3:
        answer.append(3)

    return answer