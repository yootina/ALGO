# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
# 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]



def solution(arr):

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0   
    return 1

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))

# 처음에 if, else문으로 1, 0으로 답을 냈으나 계속 오류
# 튜터로 돌려보니까 내가 짠 코드는 arr가 대칭이 하나라도 있으면 1로 반환하더라.
# 대칭이 하나라도 있으면 1을 반환하는 것이 아니라, 모든 arr가 대칭일 때 1을 반환해야 하니까 return값으로 아예 돌려버렸다.



# 다른 사람의 풀이


def solution(arr):
    return int(arr == list(map(list, zip(*arr))))

# [(5, 192, 33),
#  (192, 72, 95),
#  (33, 95, 999)]

# ==

# [[5, 192, 33],
#  [192, 72, 95],
#  [33, 95, 999]]
