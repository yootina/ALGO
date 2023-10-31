# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다.
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때,
# 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.


def solution(box, n):
    answer = 0
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer


print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))

# 프로그래머스 다른 사람의 풀이


def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )

print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))

# 다른 사람은 람다함수 되게 잘쓰네...

import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))

# math.prod : 주어진 iterable에 대해서 모든 elements에 대해서 곱셈을 계산해서 반환한다.


 