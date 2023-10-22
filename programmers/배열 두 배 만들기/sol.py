# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []

    for i in numbers:
        number = i * 2
        answer.append(number)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))


##########################################

# 다른사람의 풀이

def solution(numbers):
    return list(map(lambda x: x * 2, numbers))