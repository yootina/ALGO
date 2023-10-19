def solution(n):

    answer = 0

    if n % 7 == 0:
        answer = n // 7
    else:
        answer = n // 7 + 1
    return answer


print(solution(7))
print(solution(1))
print(solution(15))

# 하단은 프로그래머스 다른 사람 문제 풀이

def solution(n):
    return (n - 1) // 7 + 1