# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
# arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

def solution(n):
    answer = []

    for i in range(n):
        inner_list = []
        for j in range(n):
            if i == j:
                inner_list.append(1)
            else:
                inner_list.append(0)
        answer.append(inner_list)
                
    return answer

print(solution(3))
print(solution(6))
print(solution(1))


# [[표현식 for 변수2 in 범위2] for 변수1 in 범위1]

def solution(n):
    answer = [[ 1 if i == j else 0 for j in range(n) ] for i in range(n) ]
    return answer

print(solution(3))
print(solution(6))
print(solution(1))

# 다른 사람의 풀이
# 오....


def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer

# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]

# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]


