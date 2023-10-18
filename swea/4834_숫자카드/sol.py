import sys
sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     a = list(map(int, input()))

#     counter = pass
#     for i in range(N):
#         counter[int(i)] += 1
    
#     result = 0
#     for j in range(len(counter)):
#         if result <= counter[j]:
#             result = counter[j]

#     print(result)

#########################################################

T = int(input()) # 테스트 케이스

for tc in range(1, T+1): 
    N = int(input()) # 카드의 갯수
    numbers = input() # 카드의 숫자

    counter = [0 for i in range(10)]
    # counter = [0] * 10 # => [0] + [0] + [0] + ...

    for number in numbers:
        counter[int(number)] += 1

    # print(counter)

    card_count = 0
    card_number = 0

    for idx, value in enumerate(counter):
        if card_count <= value:
            card_count = value
            card_number = idx

    print(f'#{tc} {card_number} {card_count}')