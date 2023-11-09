# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers, direction):
    answer = []

    if direction == 'right':
        answer = [numbers[-1]] + numbers[:-1]
    else:
        answer = numbers[1:] + [numbers[0]]

    return answer



print(solution([1, 2, 3],"right"))
print(solution([4, 455, 6, 4, -1, 45, 6],"left"))

# unsupported operand type(s) for +: 'int' and 'list' 라는 타입에러가 나왔다.
# 숫자랑 리스트를 더해주면 타입에러가 나는것 같아서 숫자에 리스트를 씌워줬더니 해결되었다.

# 다른 사람의 풀이

from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)


# > from collections import deque 모듈을 불러와서 사용하면 스택과 큐를 한번에 처리가 가능하다고 한다.

# >>> a = [1, 2, 3, 4, 5]
# >>> q = deque(a)
# >>> q.rotate(2)  #시계방향 회전은 양수, 그 반대는 음수
# >>> result = list(q)
# >>> result
# [4, 5, 1, 2, 3]

# deque에는 다음과 같은 메서드가 더 있다.
# appendleft(x): 데크 왼쪽에 x 추가
# popleft(): 데크 왼쪽에서 요소를 제거


