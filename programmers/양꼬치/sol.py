def solution(n, k):
    
    answer = 12000 * n + 2000 * k - (n//10 * 2000)

    return answer


print(solution(10, 3))
print(solution(64, 6))

########################

# 프로그래머스 다른 사람의 풀이 방법
