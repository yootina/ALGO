import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    P, A, B = map(int, input().split())

    a_count = 0
    l = 1
    r = P

    while True:
        a_count += 1
        C = int((l+r)/2)

        # A의 경우
        if C == A:
            break
        elif C < A:
            l = C
            r = P
        else:
            r = C

    b_count = 0
    l = 1     # 문제풀 때 변수를 다시 할당해준다고 생각하지 못함.
    r = P

    while True:
        b_count += 1
        C = int((l+r)/2)

        # B의 경우
        if C == B:
            break
        elif C < B:
            l = C
            r = P
        else:
            r = C
    

    if a_count > b_count:
        answer = 'A'
    elif b_count > a_count:
        answer = 'B'
    else:
        answer = '0'

    print(f'#{tc} {answer}')    

#############################################################



