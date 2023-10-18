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
    # 애초에 1은 포함이 되질 않으니 2부터 시작하고
    # n+1만큼 반복을 하고 간격을 2만큼 달라고 한다.
    return sum(numbers)

print(solution(10))
print(solution(4))

# sum이라는 함수를 사용해서 코드 짠 방식
# result라는 리스트를 하나 만들어서 sum함수를 사용
def solution(n):
    numbers = range(2, n+1, 2)

    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return sum(numbers)

print(solution(10))
print(solution(4))