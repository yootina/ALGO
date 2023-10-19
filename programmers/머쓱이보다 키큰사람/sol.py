def solution(array, height):
    
    answer = 0

    for i in array:
        if i > height:
            answer += 1
    return answer

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))

# 하단은 프로그래머스 다른 사람의 풀이 참조.

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)