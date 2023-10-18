import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = N개의 정수, M = M개의 합
    V = list(map(int, input().split()))

    sum_list = []
    max_list = 0
    min_list = 1000000000
    # max는 0보다 클테고 min에 0을 넣지 않는 건 0보다 작은 수는 힘드니깐

    for i in range(N-M+1):
        result = 0

        for j in range(i, i+M):
            result += V[j]
        sum_list.append(result)

    max_list = max(sum_list)
    min_list = min(sum_list)

    result = max_list - min_list

    print(f'#{tc} {result}')


###############################################
# 강사님 풀이

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    min_total = 100000000000
    max_total = 0



    # 구간합을 구하기위한 i(시작점)
    # => 뒤에 M개의 데이터를 더하기 위한 시작점
    for i in range(N-M+1):
       # print(i)
        total = 0

       # 시작점을 기준으로 오른쪽 M개의 숫자의 합
        for j in range(M):
            total = total + numbers[i+j] # => 나를 기준점으로 오른쪽에 있는 숫자들을 total에 더해줌
            
        if total < min_total:
            min_total = total
            
        if total > max_total:
            max_total = total

    result = max_total - min_total

    print(f'#{tc} {result}')


