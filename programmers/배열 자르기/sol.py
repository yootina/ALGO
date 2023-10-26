def solution(numbers, num1, num2):
    numbers = []
    numbers.strip([num1, num2])

    return result


##################################

#. slicing처리...

def solution(numbers, num1, num2):
    answer = []
    answer = numbers[num1: num2+1]
    return answer

print(solution[1, 2, 3, 4, 5], 1, 3)
print(solution[1, 3, 5], 1, 2)

# 2. 두번째방법

def solution(numbers, num1, num2):
    answer = []
    for num in range(num1, num2+1):
        answer.append(number[num])
    return answer

print(solution[1, 2, 3, 4, 5], 1, 3)
print(solution[1, 3, 5], 1, 2)
