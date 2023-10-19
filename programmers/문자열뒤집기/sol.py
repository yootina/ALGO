def solution(my_string):

    answer = my_string[ : :-1] # 슬라이싱을 사용하여 문자열을 반전

    return answer

print(solution('jaron'))
print(solution('bread'))


def solution(my_string):

    return ''.join(list(reversed(my_string)))

print(solution('jaron'))
print(solution('bread'))

