def solution(num_list):
    num_list.reverse()

    return num_list

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))

def solution(num_list):
    num_list = num_list[ : : -1]

    return num_list

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))

#################################
#. 강사님 답

def solution(num_list):
    answer = []
    num_list.reverse()
    answer = num_list
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))

# 2. 인덱스 접근

def solution(num_list):
    answer = []

    for i in range(len(num_list)):
        answer.append(num_list[len(num_list)-1-i])
    return answer

#. 3. .insert()  

def solution(num_list):
    answer = []

    for num in num_list:
        answer.insert(0, num)
    return answer

