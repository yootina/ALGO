1.
def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit():
            answer += int(char)
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))

2. 
def solution(my_string):
    answer = 0

    for string in my_string:
        try:
            answer += int(string)
        except:
            continue
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))

3.
def solution(my_string):
    answer = 0

    for string in my_string:
        if not ord('A') <= ord(string) <= ord('Z'):
        # if ord( ...)
            answer += int(char)

    return answer


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))