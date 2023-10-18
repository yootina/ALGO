import sys
sys.stdin = open('input.txt')

TC = int(input())

for i in range(TC):
    num = int(input())

    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')

# 1차원 리스트 input 받기
# numbers = input().split()

# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')

numbers = list(map(int, input().split()))

# print(numbers)

for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다.')



# 2차원 리스트 입력

N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

# print(matrix[2][0]) # => [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 표형태로 생각하는 연습, print(matrix[2][0])은 7이라는 데이터에 접근.

# 데이터 자체를 반복하기
for row in matrix:
   print(row)
    for item in row:
        print(item) # item보다는 인덱스값의 기준점을 잡아서 상하좌우를 탐색하는 방법이 좀 더 쓰임.

# 행 우선 방법 (index접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(i, j, matrix[i][j])

# 열 우선 방법 (index접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(j, i, matrix[j][i])