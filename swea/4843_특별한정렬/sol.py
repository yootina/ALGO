import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = map(int, input().split())
    numbers = list(map(int, input().split()))

    result = 0

    A_list = sorted(numbers)
    B_list = sorted(numbers, reverse = True)

    for number in zip(A_list[ :5], B_list[ :5]):
    

    print(f'#{tc} {number}')


