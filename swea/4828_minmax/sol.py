import sys
sys.stdin = open('input.txt')

T = int(input())  # T는 테스트케이스

for tc in range(1, T+1):   # 테이스케이스만큼 범위를 반복
    N = int(input())
    numbers = list(map(int, input().split()))

    # print(numbers)
    min_n = numbers[0] # min_n = 10000000
    max_n = numbers[0] # max_n = 0

    for i in range(N):
        if min_n > numbers[i]:
            min_n = numbers[i]

        if max_n < numbers[i]:
            max_n = numbers[i]

    print(f'#{tc} {max_n-min_n}')                


############################################

T = int(input())

for tc in range(1, T+1):   # 테이스케이스만큼 범위를 반복
    N = int(input())
    numbers = list(map(int, input().split()))

    min_number = 10000000
    max_number = 0

    for number in numbers:
        


