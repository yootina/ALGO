def solution(numbers):
    answer = 0

    numbers.sort(reverse = True)
    answer = numbers[0] * numbers[1]

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))