def solution(my_string):

    answer = my_string[ : :-1] # 슬라이싱을 사용하여 문자열을 반전

    return answer

print(solution('jaron'))
print(solution('bread'))



#1. answer = list(reversed(my_string))

def solution(my_string):

    answer = list(reversed(my_string))
    return ''.join(answer)
    # return ''.join(list(reversed(my_string)))

print(solution('jaron'))
print(solution('bread'))

#2. answer = my_string.reverse()

def solution(my_string):

    answer = list(my_string)
    answer.reverse()

    return ''.join(answer)

print(solution('jaron'))
print(solution('bread'))

#3. answer = reversed(my_string)

def solution(my_string):

    return reversed(my_string)

print(solution('jaron'))
print(solution('bread'))

#######################################################

# str1 = ['a', 'b', 'b', 'a', 'c']

# result = reversed(str1)
# print(str1) 
# => str1 원본데이터

# print(result) 
# => reversed 함수를 실행한 'return'결과
# map 함수와 같이 lazy한 연산이기 때문에 
# list로 변환하기 전까지는 다른 객체 형태를 띔

# print(list(result)) 
# => reversed 함수를 실행한 return 결과를 list 함수로 변환

# reversed 함수를 실행한 str1의 원본은 그대로이고 리턴한 결과는 새롭게 저장됩니다.

# print(str1.reverse())
# => reverse() 메소드는 원본데이터를 직접 수정하고 리턴이 없는 메소드입니다.

# reversed() 함수는 원본은 유지 / 결과를 리턴
# .reverse() 메소드는 원본을 변경 / 리턴이 없음