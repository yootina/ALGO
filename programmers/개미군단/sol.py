def solution(hp):
    answer = 0
    for ant in hp:
        if hp <= 0:



# 장군개미 = 5
# 병정개미 = 3
# 일개미 = 1
print(solution(23))
print(solution(24))
print(solution(999))

####################################


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