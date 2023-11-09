# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

def solution(my_string):
    answer = []

    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
        else:
            continue
    answer.sort()

    return answer


print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))

# 문제풀때 계속 숫자가 아닌 문자열을 append하고 그 문자열을 sort하는 바람에 통과가 안됬었다.
# append할 때 i를 int로 바꿔주니 통과.

# 다른 사람의 풀이


def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

# 여전히 한줄로 쓰는 코드는 익숙치않다.

