def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.extend([(i, n // i)])
    return len(answer)

print(solution(20))
print(solution(100))

#################################

def solution(n):
    answer = 0
    for num in range(1, n+1):
        if n % num == 0:
            answer += 1
    return answer

print(solution(20))
print(solution(100))


# 하단은 프로그래머스 다른 사람 풀이 참조

def solution(n):
    return len([number for number in range(1, n+1) if n%number == 0])

