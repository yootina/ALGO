# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
# 문자열 my_string이 매개변수로 주어질 때
# 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    
    vowel = 'a, e, i, o, u'
    for char in vowel:
        my_string = my_string.replace(char, '')

    return my_string

print(solution("bus"))
print(solution("nice to meet you"))
# 실행한 결괏값 "nctmty"이 기댓값 "nc t mt y"과 다릅니다.

def solution(my_string):
    
    answer = ''
    vowel = ('a, e, i, o, u')
    for char in my_string:
        if char not in vowel:
            answer += char

    return answer
print(solution("bus"))
print(solution("nice to meet you"))

def solution(my_string):
    
    vowels_str = 'a,e,i,o,u'
    vowel = vowels_str.split(',')
    # vowel = ['a','e','i','o','u']

    for char in vowel:
        if char in my_string:
            my_string = my_string.replace(char, '')
      
    return my_string

print(solution("bus"))
print(solution("nice to meet you"))

# split 함수는 문자열을 특정 구분자(delimiter)를 기준으로 분리하여 리스트로 반환하는 역할
##########################################################

# 다른 사람의 풀이

def solution(my_string):
    return "".join([i for i in my_string if not i in "aeiou"])

print(solution("bus"))
print(solution("nice to meet you"))