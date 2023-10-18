import sys
sys.stdin = open('input.txt')

T = int(input())  # txt 파일에서 들고온거라 글자형태이기 였기 때문에 숫자로 변환

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))


    print(numbers)

# 1.숫자를 세워주기 위해서는 배열을 하나 만든다.
# => counter
# 리스트 컴플레이션 list안에다가 for문을 만드는 구조
# 2. 들어있는 데이터만큼 숫자를 표시해주기
# 글자 데이터이기 때문에 반복처리를 해준다함.
# 3. 숫자가 3이상이라면 똑같은 카드가 3장이라는 소리고 혹은 어떤 숫자를 기준점으로 삼아서 확인해도 됨.

# while구문으로 처리

# 리스트에서 제일 중요한것은 어떤 범위를 돌 때 인덱스 아웃오브레인지라는 것을 예상해야됌.

####################################################################################

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()

    # counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = [0 for i in range(10)]

    for number in numbers:
        counter[int(number)] += 1

    # print(counter)

    idx = 0
    is_babygin = 0

    while idx < len(counter):
        # 1. triplet인지 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1

        # 2. run인지 검증 (나를 기준으로 오른쪽 세개를 볼꺼야)
        if idx < len(counter) - 2:                         
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
        
        idx += 1

    if is_babygin == 2:
        print(True)
    else:
        print(False)