import sys
sys.stdin = open('input.txt')

# T = 10

# for tc in range(1, T+1):
#     tc = int(input()) # 테스트 케이스 번호

#     matrix = [] # 하나의 배열을 생성

#     numbers = list(map(int, input().split()))
#     matrix.append(numbers)

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
    
#     print(i, j, matrix[i][j])

# # .... 너무 어렵다.......

######################################################

# 강사님 풀이

T = 10

for tc in range(1, T+1):
    tc = int(input())

    matrix = []

    # i, j, a 반복문들 돌리는 변수를 지정
    # _는 언제 사용하냐면, 반복문에서 해당하는 변수를 사용하지 않는 경우
    for _ in range(100):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    max_total = 0

    # 시작점을 기준으로 한줄을 반복처리
    # 가로줄
    for row in range(len(matrix)):
        total = 0
        for col in range(len(matrix[0])):
            total += matrix[row][col]

        if max_total < total:
            max_total = total
    # 세로줄
    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]

        if max_total < total:
            max_total = total
    
    # 좌상단 => 우하단 대각선

    total = 0
    for i in range(100):
        total += matrix[i][i]

    if max_total < total:
        max_total = total
    
    # 우상단 -> 좌하단 대각선 

    total = 0
    for i in range(100):
        total += matrix[i][99-i]
    
    # Q. 99-i가 이해가 안됌.
    if max_total < total:
        max_total = total

    print(max_total)