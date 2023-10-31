# 가장 큰 단위를 나눠주는 방식으로 접근

def solution(hp):
    answer = 0

    a, b = divmod(hp, 5)
    hp = b
    answer += a
    
    a, b = divmod(hp, 3)
    hp = b
    answer += a

    answer += hp

    return answer


print(solution(23))
print(solution(24))
print(solution(999))

# 프로그래머스 다른 사람의 풀이


def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)



def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer



