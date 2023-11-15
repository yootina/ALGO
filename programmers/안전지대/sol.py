

def solution(board):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            # 현재 위치가 안전한 지역일 경우
            if board[i][j] == 0:  
                safe = True
                # 상하 방향으로 이동
                for dx in [-1, 0, 1]:
                    # 좌우 방향으로 이동
                    for dy in [-1, 0, 1]:
                        # 상하 및 좌우로 이동한 새로운 위치
                        ni, nj = i + dx, j + dy
                        # 방향 다 탐색하고 지뢰가 있으면
                        if 0 <= ni < len(board) and 0 <= nj < len(board[i]) and board[ni][nj] == 1:
                            safe = False
                            break
                if safe:
                    answer += 1
    return answer





print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))

# 아니 진짜 너무 어려운데;;;



