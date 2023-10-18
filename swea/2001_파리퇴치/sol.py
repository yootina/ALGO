import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly = [ list(map(int, input().split())) for _ in range(N) ]
    # print(fly)

    max_total = 0

    # 파리채를 휘두를 수 있는 공간 설정하기
    for i in range(N-M+1):
        # print(i)
        for j in range(N-M+1):

            count = 0

            # 사각형 크기       
            for x in range(i, i+M):
                for y in range(j, j+M):
                    count = count + fly[x][y]
                    
                if max_total < count:
                    max_total = count

    print(f'#{tc} {max_total}')


# 시작점을 기준으로 인덱스값을 어디로 포인트를 잡을지 생각해야됌.

#############################################################

for tc in range(1, T+1):
    # N : 전체 보드의 길이
    # M : 파리채의 길이
    N, M = list(map(int, input().split()))

    matrix = []
 
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    # print(matrix)

    total = 0
    # 파리채를 그리기 위한 기준점을 잡기위한 반복문
    for i in range(N-M+1):
        for j in range(N-M+1):

            temp = 0
            # 파리채를 그리는 반복문
            for row in range(M):
                for col in range(M):
                    temp += matrix[i+row][j+col]

            if total < temp:
                total = temp
    
    print(total)
                

         
