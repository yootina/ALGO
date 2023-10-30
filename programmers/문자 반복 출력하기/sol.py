# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string, n):
    answer = []

    for char in my_string:
        answer.append(char * n)

    return ''.join(answer)


print(solution("hello", 3))


def solution(my_string, n):
    answer = ''

    for char in my_string:
        answer += (char * n)

    return answer

print(solution("hello", 3))

# 프로그래머스 다른 사람의 풀이
# 난 아직 한줄로 하기가 어렵다...


def solution(my_string, n):
    return ''.join(i*n for i in my_string)

