def solution(my_string, letter):
    answer = ''
    answer = my_string.replace(letter, '')
    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))

# 2. 두번째방법

def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
             answer += string # 특정한 문자를 제거한다는것은 특정한 문자를 빼고 합한다라는 말.
    return answer

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))

