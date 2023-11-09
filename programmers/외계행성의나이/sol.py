# a는 0, b는 1, c는 2, ..., j는 9

def solution(age):
    answer = ''
    str_962 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    for i in str(age):
        answer += str_962[int(i)]

    return answer


print(solution(23))
print(solution(51))
print(solution(100))

# 다른 사람의 풀이를 봤는데 이건 뭐지? 싶었다.

# 다른 사람의 풀이

def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])

# chr()를 이용하여 아스키코드를 대입한다.
# 나이를 str형으로 바꿔주고, 각 요소를 다시 int형으로 바꿔 준 다음에 chr()에 넣는다.

# chr()는 아스키코드를 문자열로 반환하는 함수
# 괄호( ) 안에 숫자를 넣으면 그 숫자의 아스키코드에 대응하는 문자를 반환한다.
# 97:a, 98:b ... 106:j

# ord() 반대로 문자열을 아스키코드로 반환하는 함수이다.
# 괄호( ) 안에 문자를 넣으면 그 문자에 해당하는 아스키코드를 숫자로 반환한다.

# chr() 함수를 이용해서 아스키코드를 문자열로 반환해주는게 놀랍다!


