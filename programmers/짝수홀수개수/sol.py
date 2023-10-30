# 정수가 담긴 리스트 num_list가 주어질 때,
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    answer = []

    num1 = 0
    num2 = 0
    for i in num_list:
        if i % 2 == 0:
            num1 += 1
        else:
            num2 += 1

    answer.extend([num1, num2])
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))


# 프로그래머스 다른 사람의 풀이
# 그냥 미친 풀이같다 ㅎ

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))
