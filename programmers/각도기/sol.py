def solution(angle):

    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4

print(solution(70))
print(solution(91))
print(solution(180))

######################################
# 강사님 답

def solution(angle):
    answer = 0
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    else:
        answer = 4

    return answer

print(solution(70))
print(solution(91))
print(solution(180))