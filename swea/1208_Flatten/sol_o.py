import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T+1):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        
        max_box = box.index(max(box))
        box[max_box] -= 1

        min_box = box.index(min(box))
        box[min_box] += 1
    
    result = max(box) - min(box)
    
    print(f'#{tc} {result}')

# 단순히 최댓값의 인덱스를 구하고 최솟값의 인덱스를 구해서 +=, -=씩 해준다고 생각했다.
# 마지막엔 최댓값과 최솟값의 차이를 구해서 출력해주었다.
# 출력값이 맞아서 다행이다.

############################################

# 강사님 풀이
# 강사님께서는 처음코딩하는 학생들을 위해 어떤방식으로 작동하는지 자세히 가르쳐주셨다.

T = 10

for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # while dump > 0:
    #   dump -= 1
    for i in range(dump):

        # 최대높이
        top_box = boxes[0]  # => boxes[0]번째 데이터가 가장 크다고 가정하고 시작
        top_box_idx = 0

        # 최소높이
        down_box = boxes[0]
        down_box_idx = 0

        # 최대와 최소 높이 찾기
        for i in range(len(boxes)):
            if top_box < boxes[i]:
                top_box = boxes[i]
                top_box_idx = i

            if down_box > boxes[i]:
                down_box = boxes[i]
                down_box_idx = i

        # top_box = max(boxes)
        # down_box = min(boxes)
        # 최대와 최소높이 구하기는 위와 같이 사용해도 무방.

        # 최댓값과 최솟값을 찾았으면 그 다음엔 평탄화작업이 필요.

        # 평탄화
        boxes[top_box_idx] -= 1
        boxes[down_box_idx] += 1

        # 전체 평탄화 횟수 전에 평탄화가 완료된 경우
        if boxes[top_box_idx] - boxes[down_box_idx] < 1:
            break

    result = max(boxes) - min(boxes)

    print(f'#{tc} {result}')

        