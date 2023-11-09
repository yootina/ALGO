# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []

    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
        answer.sort()
    return answer


print(solution(24))
print(solution(29))

# 오,,,, 뭐야,,,, 쉽게 풀어버렸는데 다른 사람도 쉽게 풀었겠지..?

