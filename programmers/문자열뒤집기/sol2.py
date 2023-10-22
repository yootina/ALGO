def solution(my_string):

    answer = list(reversed(my_string))
    return ''.join(answer)
print(solution('jaron'))

def solution(my_string):

    return ''.join(reversed(my_string))

print(solution('jaron'))
#################################################


def solution(my_string):

    answer = list(my_string)
    answer.reverse()
    return ''.join(answer)

print(solution('jaron'))