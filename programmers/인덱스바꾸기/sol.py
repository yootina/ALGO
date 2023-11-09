# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string, num1, num2):
    answer = ''
    str_list = []

    for i in range(len(my_string)):
        if i == num1:
            str_list.append(my_string[i]) # e, l
        elif i == num2:
            str_list.append(my_string[i])
        
    # replace로 해보려했으나 구현이 안됐다.
    answer = my_string[:num1] + str_list[1] + my_string[num1 + 1:num2] + str_list[0] + my_string[num2 + 1:]
    return answer




print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))

