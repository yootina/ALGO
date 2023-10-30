# 문제 다시 풀어보기

def solution(keyinput, board):
    row = board[0]
    col = board[1]

    result = [0, 0]

    for i in keyinput:
        if i == 'left' and result[0]-1 >= -(row // 2):
            result[0] -= 1
        elif i == 'right' and result[0]+1 <= (row // 2):
            result[0] += 1
        elif i == 'up' and result[1]+1 <= (col // 2):
            result[1] += 1
        elif i == 'down' and result[1]-1 >= -(col // 2):
            result[1] -= 1
    return result 

print(solution(["left", "right", "up", "right", "right"],[11, 11]))
print(solution(["down", "down", "down", "down", "down"],[7, 9]))




# 다른 사람의 풀이

def solution(keyinput, board):
    answer = [0, 0]
    temp = [0, 0]
    width, length = board[0]//2, board[1]//2
    move = {'left': [-1, 0],
            'right': [1, 0], 
            'up': [0, 1], 
            'down': [0, -1],
           }
    for key in keyinput:
        temp = [x + y for x, y in zip(answer, move[key])]  
        if abs(temp[0]) > width or abs(temp[1]) > length:
            continue
        else:
            answer = [x + y for x, y in zip(answer, move[key])]                   
    return answer
