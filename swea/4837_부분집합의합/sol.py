import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 부분 집합 원소의 개수
    # K : 부분 집합 원소의 총 합
    N, K = map(int, input().split())

    numbers = [ i for i in range(1, 13)]
    n = len(numbers)

    # 부분집합의 경우의수 찾아보기
    for i in range(1<<n):

        arr = []
        # 모든 부분집합을 찾아보기
        for j in range(n):
            arr.append(numbers[j])


#################################################
#. 강사님 풀이

# N : 부분 집합 원소의 개수
# K : 부분 집합 원소의 총 합

for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))

    count = 0

    for i in range(1 << len(numbers)):
        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])

        if len(temp) == N and sum(temp) == K:
            count += 1

    print(count)