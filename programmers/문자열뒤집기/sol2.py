def solution(my_string):

    answer = list(reversed(my_string))
    return ''.join(answer)

print(solution('jaron'))



def solution(my_string):

    return ''.join(reversed(my_string))

print(solution('jaron'))
#################################################

# 리스트의 요소를 역순으로 만들어 준다.(리스트 메서드)
# 그러므로 숫자나 문자열 그리고 튜플에서는 사용할 수 없다. 
# 리스트.reverse()

def solution(my_string):

    answer = list(my_string)
    answer.reverse()
    return ''.join(answer)

print(solution('jaron'))