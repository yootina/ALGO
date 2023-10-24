# 머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다.
# 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며,
# 편지를 가로로만 적을 때, 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를
# return 하도록 solution 함수를 완성해주세요.


def solution(message):
    answer = 0
    message_list = []

    for char in message:
        message_list.append(char)
        answer = len(message_list) * 2
       
    return answer

print(solution("happy birthday!"))
print(solution("I love you~"))

# 처음에 아직 개념이 잡혀있지 않아서 for char in range(len(message)) 식으로 작성을 했다
# 파이썬 튜터에 돌려보니 인덱스번호를 리스트에 넣고 answer에는 리스트의 길이를 2배 반환해서 결과는 같게 나왔지만
# 다시 생각해보니 문자열을 굳이 인덱스번호로 넣지않아도 리스트로 만들수 있으니
# 문자열을 올바르게 처리하고 보다 직관적인 방식으로 작성 되게 변경하였다.

#############################################################################

# 프로그래머스 다른 사람의 풀이

def solution(message):
    return len(message)<<1

# 오... 비트연산에 대해서 배웠는데 생각치도 못했다...

def solution(message):
    return len(message)*2

# 이렇게 쉽게 작성할 수 있었던거였구나 ㅠㅠ 반성한다 내 자신.
