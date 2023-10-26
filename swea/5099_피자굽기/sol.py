import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    pizza_list = []


    for i in range(M): # 피자개수만큼 반복문을 돌린다면 (아래는 피자에 번호를 붙이는 반복문)
        pizza_list.append([i+1, Ci[i]]) # 피자리스트에 피자번호와 치즈의 양을 더해준다
    # print(pizza_list)
    # 인덱스 번호를 이용해서 화덕의 피자와 치즈의 양을 유추한다.

    oven = pizza_list[ :N]
    pizza_b = pizza_list[N: ]
    # print(oven)
    
    while len(oven) != 1: # 오븐에 피자가 하나남을때까지 반복문

        see = oven.pop(0)  # 맨앞에 피자를 보려고 꺼낸다

        if see[1] // 2 == 0:  # 보고있는 피자의 [1]번째 (치즈)가 0이 되었을 때
            if pizza_b > 0:   # 남아있는 피자가 있다면
                oven.append(pizza_b.pop(0)) # 남아있는 피자의 0번째를 오븐에 더한다.
        else:
            oven.append(see)   #치즈가 남아있다면 보고있는 피자는 다시 오븐에 더해준다.

# print(f'#{tc} {oven[0][0]}')

################################################################

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    Ci = list(map(int, input().split()))

    # print(N, M, Ci)

    # 피자에 번호를 붙여주는 과정
    before = []
    for i in range(M):
        before.append([Ci[i], i])

    # 화덕
    queue = [0] * N

    after = []

    # 완성피자가 구워야 하는 피자 갯수랑 같아질때까지 반복
    while len(after) != M:

        # 화덕입구에 공간이 비었으면
        if queue[0] == 0:
            # 넣을 피자가 있으면
            if len(before) != 0:
                # 남은 첫번째 피자의 치즈의 양과 번호
                cheeze, idx = before.pop(0)
                # 화덕에 넣기
                queue.append([cheeze, idx])
                # 화덕 돌리기
                queue.pop(0)
            # 넣을 피자가 없는경우
            else:
                # 화덕 돌리기
                queue.pop(0)
                queue.append(0)

        # 화덕입구에 공간이 비어있지 않다면(이미 구워지고 있는 피자가 있는경우)
        else:
            # 치즈를 절반 감소
            queue[0][0] //= 2

            # 치즈가 다 녹은경우
            if queue[0][0] == 0:
                pizza = queue.pop(0)
                # 완성목록에 넣기
                after.append(pizza)

                # 화덕의 길이가 줄었기 때문에
                # 상황에 맞춰서 화덕을 똑같은 길이로 유지
                
                # 더이상 만들 피자가 없는경우
                if len(before) == 0:
                    queue.append(0)
                # 피자를 더 넣어야 하는경우
                else:
                    cheeze, idx = before.pop(0)
                    queue.append([cheeze, idx])

            # 치즈가 남아있는경우 (더 돌려야 하는경우)
            else:
                # 화덕 돌리기
                pizza = queue.pop(0)
                queue.append(pizza)


    print(after[-1][1] + 1)