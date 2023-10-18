# def solution(n):
#     answer = 0
#     return answer

# result = 1 + 2 + 3 + 4 = 10
# result = 9 + 3 + 0 + 2 + 1 + 1 = 16


def solution(n):
    result = 0
    for number in str(n):
        result += int(number)
    return result

print(solution(1234))
print(solution(930211))

#################################

# 1. (나눗셈)

def solution(n):
    answer = 0

    while n > 0:
        # a: 몫, b: 나머지
        a = n // 10
        b = n % 10

        n = a
        answer += b
    return answer

print(solution(1234))
print(solution(930211))

# 2. n을 반복처리

def solution(n):
    answer = 0

    for i in str(n): # int는 반복처리할수없다.
        answer += int(i)
    return answer
    
print(solution(1234))
print(solution(930211))