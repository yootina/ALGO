def solution(keyinput, board):
    row = board[0]
    col = board[1]
    answer = [0, 0]

    for i in keyinput:
        if i == "left" and answer[0]-1 >= -(row // 2):
            answer[0] = answer[0] - 1
        elif i == "right" and answer[0]+1 <= (row // 2):
            answer[0] = answer[0] + 1
        elif i == "up" and answer[1]+1 <= (col // 2):
            answer[1] = answer[1] + 1
        elif i == "down" and answer[1]-1 >= -(col // 2):
            answer[1] = answer[1] - 1

    return answer


print(solution(["left", "right", "up", "right", "right"],[11, 11]))
print(solution(["down", "down", "down", "down", "down"],[7, 9]))