# 내가 적은 식

def solution(n):
    answer = 0

    for number in range(n + 1):
        if number % 2 == 0:


    return answer

########################
# 강사님이 적은 식
# 짝수를 모두 더한 값이라면 짝수를 먼저 구하고 짝수의 합을 구하기

def solution(n):
    answer = 0

    numbers = range(1, n+1)
    for number in numbers:
        if number % 2 == 0:
            answer = answer + number

    return answer

print(solution(10))
print(solution(4))

################################
# 강사님이 적은 식
# 좀 더 간결하게

def solution(n):
    numbers = range(2, n+1, 2)
    return sum(numbers)

print(solution(10))
print(solution(4))
