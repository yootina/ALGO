# 문자열 my_string이 매개변수로 주어질 때,
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''

    for char in my_string:
        if char.isupper() == True:
            answer += char.lower()
        else:
            answer += char.upper()
    return answer



print(solution("cccCCC"))
print(solution("abCdEfghIJ"))

# 프로그래머스 다른 사람의 풀이

def solution(my_string):
    return "".join(map(lambda s: s.upper() if s.islower() else s.lower(), my_string))

