def solution(dot):

    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4


print(solution([2, 4]))
print(solution([-7, 9]))



# 프로그래머스 다른 사람의 풀이

def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

# 이 코드는 그냥 미쳤다....

def solution(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2
    
# 오우.. 생각도 못했다