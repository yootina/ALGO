# 머쓱이는 친구들과 369게임을 하고 있습니다.
# 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신
# 3, 6, 9의 개수만큼 박수를 치는 게임입니다.
# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때,
# 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

def solution(order):
    answer = 0

    for i in str(order):
        if i in ['3', '6', '9']:
            answer += 1

    return answer


print(solution(3))
print(solution(29423))


# 다른 사람의 풀이
# 어렵다.. 람다...

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

# map: 함수와 리스트를 인자로 받는다
# 리스트에서 하나씩 꺼내서 함수를 적용시킨다.
# str(order): 입력으로 받은 order를 문자열로 바꾸고, 리스트[3, 6, 9]의 각 숫자를 문자열로 바꾼다.
# lambda x: str(order).count(str(x)): 3,6,9 숫자가 문자열로 바뀐 order에서 몇 번 나오는지를 세어본다.
# map함수로 적용한다.
# sum으로 개수를 모두 더하여 반환한다.
