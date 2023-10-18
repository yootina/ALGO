import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # N개의 영역에 칠하는개수

    # 리스트로 영역(표)만들기
    temp = [ [0] * 10 for _ in range(10) ]
    purple = 0

    # N개만큼 반복문 돌리기
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 색칠하기..... 시작.....
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if temp[i][j] == 0:      # 2차원 리스트 N영역에 값이 0이라면 컬러가 없으니 컬러를 더해주기
                    temp[i][j] = color
                else:
                    purple += 1

    print(f'#{tc} {purple}')
    