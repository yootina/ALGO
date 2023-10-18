import sys
sys.stdin = open('input.txt')

T = 10

for tc in (1, T+1):
    result = 0
    N = int(input()) # 건물의 개수
    buildings = list(map(int, input().split())) # 건물의 높이
    
    for i in range(2, N-2):

        left = max(buildings[i-1], buildings[i-2])
        right = max(buildings[i+1], buildings[i+2])
        max_building = max(left, right)

        count = buildings[i] - max_building
        result += count

    print(f'#{tc} {result}')

# 뭔가 잘못됌..
# 범위설정이 잘못생각하고 있었음
# 가장 큰 건물을 설정을 안하고 있었음.

############################################################

# 문제의핵심: 1. 맨 왼쪽에 있는 2칸과 맨 오른쪽에 있는 2칸이 비어있다.

T = 10

for tc in (1, T+1):
    result = 0
    N = int(input()) # 건물의 개수
    buildings = list(map(int, input().split())) # 건물의 높이

    total = 0

    for i in range(N):
        now = buildings[i]

        # 현재위치에 건물이 없는 경우
        if now == 0:
            continue

        # 현재위치에 건물이 없는 경우
        else:
            dx = [-2, -1, 1, 2] # 델타x = dx

            max_tall = 0

            # 중심을 기준으로 4개의 건물 중 가장 큰 건물을 고르기
            for j in range(4):
                # i (now) : 현재위치(기준점)
                # dx[j] : 기준 건물을 중심으로 좌우 인덱스

                comp = buildings[i+dx[j]]

                if max_tall < comp:
                    max_tall = comp

            # 나머지 4개의 건물보다 현재 건물의 높이가 크다면
            # 조망권 확보!
            if now > max_tall:
                view = now - max_tall
                total += view

    print(f'#{tc} {total}')