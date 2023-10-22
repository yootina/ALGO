# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면
# 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

def solution(slice, n):
    answer = 0

    if n % slice == 0:
        answer = n // slice
    elif n % slice != 0:
        answer = (n // slice) + 1
    return answer

print(solution(7, 10))
print(solution(4, 12))

##################################

# 다른 사람의 풀이

def solution(slice, n):
    return ((n - 1) // slice) + 1


################################

def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)

print(solution(7, 10))


##################################

import math

def solution(slice, n):
    return math.ceil(n/slice)

# math 모듈
# - 수학과 관련한 함수를 모아놓은 모듈

# - import math
# math.ceil()
# - 소수점 이하의 수를 올림하여 정수로 반환하는 함수

# math.floor()
# - 소수점 이하의 수를 내림하여 정수로 반환하는 함수