import sys
sys.stdin = open('input.txt')

T = int(input())   # 테스트 수 #(1 <= T <= 50)

for tc in range(1, T+1):
    # K = 최대로 이동가능한 정류장 수
    # N = 정류장 갯수
    # M = 충전기가 있는 정류장 수
    K, N, M = map(int, input().split()) # (1 <= K,N,M <= 100)

    station = list(map(int, input().split())) # 충전기가 위치한 정거장번호
    # print(station)
    # location = [0 for i in range(N+1)] # 버스의 현재 위치

    for i in station:
        location += 1





###########################################################################

T = int(input())

for tc in range(1, T+1):
    # K : 최대로 이동 가능한 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수

    K, N, M = list(map(int, input().split()))

    bus_stop = list(map(int, input().split()))

    count = 0
    now = 0

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0
    # 충전을 하면서 지나가야 하는 경우
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속 반복
        while now < N:
            # 현재위치(now)를 기준으로 최대로 갈 수 있는 범위를 찾는다.
            for i in range(now+K, now, -1):
                # 1. 최대범위가 종점을 넘는경우
                if i >= N:
                    now = N
                    break

                # 2. 최대범위가 종점을 넘지 않은경우
                if i in bus_stop:
                    now = i
                    count += 1
                    break

            # 현재 위치에서 최대 거리까지 다 확인을 했는데 충전소가 없다면 => 도착 불가능
            else:
                count = 0
                now = N

    print(f'#{tc} {count}')


#########################################################

#. 강사님과 접근이 비슷하지만 다른 코드

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    K, N, M = list(map(int, input().split()))  #설명에 나와있듯 첫번째는 K(1회 충전 당 이동할 수 있는거리), N(도착해야하는 위치), M(정류소 갯수)

    charge_station = list(map(int, input().split()))  #charge_station을 호출했으니 사실상 M이라는 변수는 이제 생각 안해도 될듯

    count = 0

    current = 0

    while current + K < N:  #현재위치에서 한번에 이동 가능한 K를 합한 값이 내가 도착해야하는 위치보다 클 때 루프 종료

        for move in range(K, 0, -1): #K만큼 움직이다 충전소가 있는 K-(가장 작은 수)에 충전소가 있으면 충전을 해야하니 K~0까지 -1
    
            if (current + move) in charge_station: 
                current += move                     #현재위치에서 충전소까지 이동했으니 현재 위치는 충전소이다.
                count += 1                          #충전소에서 충전을 했으면 1회 count

                break
        else:                                      #움직이는 거리 안에 충전소가 없다면 count x = 도착 x
            count = 0
            break
    
    print(f'#{tc} {count}')

    