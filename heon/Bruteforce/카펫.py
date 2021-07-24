def solution(brown, yellow):
    answer = []

    temp = brown + 4

    height_width = temp // 2

    for height in range(3, height_width // 2 + 1):
        width = height_width - height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]